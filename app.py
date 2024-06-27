import streamlit as st
import pandas as pd
import base64


def levenshtein_distance(token1, token2):
    distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                distances[t1][t2] = min(a, b, c) + 1

    return distances[len(token1)][len(token2)]


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


def main():
    st.title("Word Correction using Levenshtein Distance")

    # File uploader for custom vocabulary
    uploaded_file = st.file_uploader("Upload a vocabulary file", type="txt")
    if uploaded_file:
        vocabs = load_vocab(uploaded_file)
    else:
        vocabs = load_vocab(file_path='./vocab.txt')

    word = st.text_input('Enter a word:')
    num_suggestions = st.slider('Number of suggestions:', 1, 10, 5)

    if st.button("Compute"):
        # Compute Levenshtein distances
        leven_distances = {vocab: levenshtein_distance(word, vocab) for vocab in vocabs}

        # Sort by distance
        sorted_distances = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
        suggestions = list(sorted_distances.items())[:num_suggestions]

        st.write(f"Top {num_suggestions} suggestions:")
        for suggestion, distance in suggestions:
            st.write(f"{suggestion} (Distance: {distance})")

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.table(pd.DataFrame(vocabs, columns=['Word']))

        col2.write('Distances:')
        col2.table(pd.DataFrame(sorted_distances.items(), columns=['Word', 'Distance']))

    # Option to download the vocabulary as a text file
    if st.button("Download Vocabulary"):
        vocab_str = '\n'.join(vocabs)
        b64 = base64.b64encode(vocab_str.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="vocab.txt">Download Vocabulary</a>'
        st.markdown(href, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
