# ATS Score Calculify

## Overview

**ATS Score Calculify** is a web application designed to evaluate resumes against job descriptions using advanced AI models. It offers three main functionalities:

- **Resume Evaluation:** Review the provided resume against the job description and highlight strengths and weaknesses.
- **Improvement Suggestions:** Provide constructive feedback on the resume and suggest improvements.
- **Match Percentage Calculation:** Analyze the resume and job description to give a percentage match, along with missing keywords and final thoughts.

This tool is built using Streamlit for the user interface and Google Generative AI for processing and analyzing the content.

## Features

- **Evaluate Resume:** Get a professional evaluation of how well the resume matches the job description.
- **Suggest Improvements:** Receive actionable feedback to improve the resume.
- **Percentage Match:** Calculate the percentage of match between the resume and the job description.
- **Progress Indicator:** Shows a spinner while processing the PDF.
- **Visualizations:** Displays a bar chart showing the match percentage.
- **File Handling:** Handles PDF file uploads and ensures file integrity.

## Installation

To set up the project on your local machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ats-score-calculify.git
cd ats-score-calculify

### 2. Create a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

- **Windows:**

  ```bash
  .venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source .venv/bin/activate
  ```

### 4. Install Dependencies

Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the project root directory and add your Google Generative AI API key:

```makefile
GOOGLE_API_KEY=your_google_api_key
```

### 6. Add Poppler to PATH

Ensure that Poppler is installed and added to your PATH environment variable. Download it from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/) or the [Poppler official website](https://poppler.freedesktop.org/).

Add the Poppler `bin` directory to your PATH:

- **Windows:**

  Open Command Prompt and run:

  ```bash
  set PATH=%PATH%;C:\Program Files\Poppler\Library\bin
  ```

- **macOS/Linux:**

  Add the following line to your `.bashrc` or `.zshrc` file:

  ```bash
  export PATH="/path/to/poppler/bin:$PATH"
  ```

  Replace `/path/to/poppler/bin` with the actual path to the Poppler `bin` directory.

### 7. Run the Application

Start the Streamlit server with:

```bash
streamlit run app.py
```

Open your web browser and navigate to [http://localhost:8501](http://localhost:8501) to access the application.

## Usage

### 1. Enter Job Description

In the "Job Description" text area, input the job description for the role you are evaluating.

### 2. Upload Resume

Upload the resume in PDF format using the "Upload Resume" button.

### 3. Select an Action

Choose one of the following actions:

- **Evaluate Resume:** Click "Evaluate Resume" to receive a professional evaluation of the resume.
- **Suggest Improvements:** Click "Suggest Improvements" for feedback on how to enhance the resume.
- **Percentage Match:** Click "Percentage Match" to get the match percentage along with keywords missing and final thoughts.

### 4. View Results

Results will be displayed on the page based on the selected action. If you choose "Percentage Match," a bar chart showing the match percentage will also be displayed.

## Troubleshooting

### Common Issues

- **Empty PDF File:** Ensure that the PDF file is not empty.
- **File Upload Errors:** Check that the file is indeed a PDF and not corrupted.
- **API Key Errors:** Verify that the `GOOGLE_API_KEY` in your `.env` file is correct and valid.
- **Poppler Issues:** Make sure that Poppler is correctly installed and the `bin` directory is in your PATH.

### Error Messages

- **`PDFPageCountError`**: This usually means the PDF file is empty or corrupted. Check the file and ensure it’s a valid PDF.
- **`ValueError: could not convert string to float`**: This indicates a parsing issue. Make sure the response text from the API contains a valid percentage.

## Acknowledgements

- [Streamlit](https://www.streamlit.io/) for creating an excellent tool for building web apps.
- [Google Generative AI](https://cloud.google.com/generative-ai) for advanced AI capabilities.
- [pdf2image](https://pypi.org/project/pdf2image/) for PDF to image conversion.
- [Poppler](https://poppler.freedesktop.org/) for PDF rendering.

