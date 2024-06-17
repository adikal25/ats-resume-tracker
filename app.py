import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def gemini_response(resume_text, job_description):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt_template = f"""
    You are an expert resume reviewer. Analyze the provided resume for alignment with the job description. 
    Evaluate content relevance, clarity, and impact. Assess formatting for readability and consistency. Check language for professionalism and conciseness. 
    Identify gaps, suggest improvements, and provide actionable feedback to enhance the resume’s effectiveness and match the job requirements. 
    Offer specific examples for revision. You must consider the job market is very tough and suggest any up skills required and 
    also missing keywords to matching job Description
    resume:{resume_text}
    description={job_description}
    i want a response in a bullet points 
    {{
        "JD Match":"%",
        "Missing Keywords":[],
        "Profile Summary" : "",
        "Upskills required" : ""
    }}
    """
    gemini_response = model.generate_content(prompt_template)
    return gemini_response.text


def convert_pdf_text(file):
    reader = pdf.PdfReader(file)
    text = " "
    for page in reader.pages:
        text += str(page.extract_text())
    return text


st.title("Resume.ai")
st.text("Improve your Resume According to the job description")
jd = st.text_area("Paste the required job description")
file = st.file_uploader("Upload your Resume", type="pdf",
                        help="Please only upload a pdf")

submit = st.button("Analyze")

if submit:
    if file is not None:
        text = convert_pdf_text(file)
        response = gemini_response(text, jd)
        st.subheader(response)
