from dotenv import load_dotenv
import streamlit as st
import os
import io
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Add poppler to PATH
os.environ['PATH'] += os.pathsep + r'C:\Program Files\Poppler\Library\bin'

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Google Generative AI
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# Function to process the uploaded PDF
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App Configuration
st.set_page_config(page_title="ATS Score Calculify", page_icon=":briefcase:", layout="centered")
st.title("ATS Score Calculify")
st.markdown("""
    <style>
        .main {
            background-color: black;
        }
        h1 {
            color: orange;
        }
        .stTextInput, .stFileUploader, .stButton, .stTextArea {
            margin-bottom: 20px;
        }
        .stTextArea label {
            font-size: 16px;
            font-weight: bold;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px; 
        }
   
    </style>
""", unsafe_allow_html=True)

# User Inputs
# st.header("Applicant Tracking System")
st.subheader("Job Description")
input_text = st.text_area("Enter the job description here:", key="input", height=150)

st.subheader("Upload Resume")
uploaded_file = st.file_uploader("Upload your resume (PDF):", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully")

# Prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an experienced career coach. Your task is to provide constructive feedback on the resume provided. 
Please suggest improvements that can be made to the resume to better match the job description. 
Highlight any areas where the candidate can improve their skills or experience.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches 
the job description. First, the output should come as percentage and then keywords missing and last, final thoughts.
"""

# Buttons
submit1 = st.button("Evaluate Resume")
submit2 = st.button("Suggest Improvements")
submit3 = st.button("Percentage Match")

# Process Evaluation
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("Evaluation Result")
        st.write(response)
    else:
        st.warning("Please upload the resume.")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("Suggested Improvements")
        st.write(response)
    else:
        st.warning("Please upload the resume.")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("Match Percentage")
        st.write(response)
    else:
        st.warning("Please upload the resume.")
