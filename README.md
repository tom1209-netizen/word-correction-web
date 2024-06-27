# Word Correction using Levenshtein Distance

This project is a Streamlit application for word correction based on Levenshtein Distance. It allows users to upload a custom vocabulary, input a word, and receive suggestions for the correct word. The application also displays the vocabulary and the computed Levenshtein distances in a tabular format.

## Features

- File uploader for custom vocabulary input
- Slider to select the number of suggestions to display
- Displays vocabulary and Levenshtein distances in tables
- Option to download the vocabulary as a text file

## Installation

To run this application, you need to have Python installed on your machine. Follow these steps to install the required libraries and run the app.

### 1. Clone the repository

```bash
git clone https://github.com/tom1209-netizen/word-correction-web.git
cd word-correction-web
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate 
```

### 3. Install the required libraries
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app
```bash
streamlit run app.py
```