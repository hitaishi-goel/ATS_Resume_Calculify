ATS Score Calculify
Overview
ATS Score Calculify is a web application designed to evaluate resumes against job descriptions using advanced AI models. It offers three main functionalities:

Resume Evaluation: Review the provided resume against the job description and highlight strengths and weaknesses.
Improvement Suggestions: Provide constructive feedback on the resume and suggest improvements.
Match Percentage Calculation: Analyze the resume and job description to give a percentage match, along with missing keywords and final thoughts.
This tool is built using Streamlit for the user interface and Google Generative AI for processing and analyzing the content.

Features
Evaluate Resume: Get a professional evaluation of how well the resume matches the job description.
Suggest Improvements: Receive actionable feedback to improve the resume.
Percentage Match: Calculate the percentage of match between the resume and the job description.
Progress Indicator: Shows a spinner while processing the PDF.
Visualizations: Displays a bar chart showing match percentage.
File Handling: Handles PDF file uploads and ensures file integrity.
Installation
To set up the project on your local machine, follow these steps:

1. Clone the Repository
bash
Copy code
git clone https://github.com/hitaishi-goel/ATS_Resume_Calculify.git
cd ats-score-calculify
2. Create a Virtual Environment
bash
Copy code
python -m venv .venv
3. Activate the Virtual Environment
Windows:

bash
Copy code
.venv\Scripts\activate
macOS/Linux:

bash
Copy code
source .venv/bin/activate
4. Install Dependencies
bash
Copy code
pip install -r requirements.txt
5. Set Up Environment Variables
Create a .env file in the project root directory and add your Google Generative AI API key:

makefile
Copy code
GOOGLE_API_KEY=your_google_api_key
6. Add Poppler to PATH
Ensure that Poppler is installed and added to your PATH environment variable. Download it from Poppler for Windows or the Poppler official website.

Add the Poppler bin directory to your PATH:

bash
Copy code
set PATH=%PATH%;C:\Program Files\Poppler\Library\bin
7. Run the Application
Start the Streamlit server with:

bash
Copy code
streamlit run app.py
Open your web browser and navigate to http://localhost:8501 to access the application.

Usage
1. Enter Job Description
In the "Job Description" text area, input the job description for the role you are evaluating.

2. Upload Resume
Upload the resume in PDF format using the "Upload Resume" button.

3. Select an Action
Choose one of the following actions:

Evaluate Resume: Click "Evaluate Resume" to receive a professional evaluation of the resume.
Suggest Improvements: Click "Suggest Improvements" for feedback on how to enhance the resume.
Percentage Match: Click "Percentage Match" to get the match percentage along with keywords missing and final thoughts.
4. View Results
Results will be displayed on the page based on the selected action. If you choose "Percentage Match," a bar chart showing the match percentage will also be displayed.

Troubleshooting
Common Issues
Empty PDF File: Ensure that the PDF file is not empty.
File Upload Errors: Check that the file is indeed a PDF and not corrupted.
API Key Errors: Verify that the GOOGLE_API_KEY in your .env file is correct and valid.
Poppler Issues: Make sure that Poppler is correctly installed and the bin directory is in your PATH.
Error Messages
PDFPageCountError: This usually means the PDF file is empty or corrupted. Check the file and ensure it’s a valid PDF.
ValueError: could not convert string to float: This indicates a parsing issue. Make sure the response text from the API contains a valid percentage.
Contributing
Contributions are welcome! If you have suggestions for improvements or find any issues, please open an issue or submit a pull request.

Acknowledgements
Streamlit for creating an excellent tool for building web apps.
Google Generative AI for advanced AI capabilities.
pdf2image for PDF to image conversion.
Poppler for PDF rendering.
