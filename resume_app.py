import streamlit as st
import pandas as pd
import re
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Streamlit Page Setup
st.set_page_config(page_title="AI Resume Screening", layout="wide")
st.title("AI Resume Screening and Candidate Ranking System")

# Job Description Input
st.subheader("Job Description")
job_description = st.text_area("Paste the job description here:")

# Resume Upload
st.subheader("Upload Resumes (PDF)")
uploaded_files = st.file_uploader("Choose PDF files", type=["pdf"], accept_multiple_files=True)

# Predefined Skills List
skills = ['python', 'java', 'c++', 'sql', 'machine learning', 'data analysis', 'communication', 'leadership']

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf = PdfReader(pdf_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text

# Analyze Button
if st.button("Analyze Resumes"):
    if job_description and uploaded_files:
        jd_vector = TfidfVectorizer().fit_transform([job_description])
        results = []

        for file in uploaded_files:
            resume_text = extract_text_from_pdf(file)
            tfidf = TfidfVectorizer().fit_transform([job_description, resume_text])
            similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

            skill_matches = sum(skill in resume_text.lower() for skill in skills)
            ats_score = (similarity * 0.7 + skill_matches / len(skills) * 0.3) * 100

            results.append({
                'Candidate': file.name,
                'Match %': round(similarity * 100, 2),
                'Skill Match': f"{skill_matches}/{len(skills)}",
                'ATS Score': round(ats_score, 2)
            })

        df = pd.DataFrame(results).sort_values(by="ATS Score", ascending=False)
        st.subheader("Ranking Results")
        st.dataframe(df.reset_index(drop=True))
    else:
        st.warning("Please enter job description and upload at least one resume.")
