# Resume.ai

Resume.ai is a Streamlit application designed to analyze resumes against job descriptions using a generative AI model from Google's Generative AI platform.

## Overview

This application allows users to upload a PDF resume and paste a job description to receive feedback on how well the resume matches the job requirements. The AI model evaluates the resume's content relevance, clarity, formatting, language professionalism, and suggests improvements such as missing keywords and required upskilling.

## Features

- **Resume Upload:** Users can upload their resume in PDF format.
- **Job Description Input:** Users can paste the job description for analysis.
- **Analysis and Feedback:** Generates a structured feedback report in bullet points:
  - JD Match percentage.
  - Missing Keywords.
  - Profile Summary suggestions.
  - Upskills required for better alignment with the job description.

## Installation

1. Clone the repository:

   ```bash
   git clone 
   cd Resume.ai

- pip install -r requirements.txt
- streamlit run app.py

