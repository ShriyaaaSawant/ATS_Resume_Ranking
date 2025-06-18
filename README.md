# AI Resume Screening and Candidate Ranking App

This project uses AI to rank resumes based on job descriptions. It mimics how ATS (Applicant Tracking Systems) filter resumes by keyword match and skills.

## Features
- Upload multiple PDF resumes
- Paste any job description
- Ranks candidates using TF-IDF + Cosine Similarity
- Calculates ATS score based on skill matching

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- PyPDF2
- Pandas

## How to Run
1. Clone this repo or download the files
2. Navigate to the folder:
cd Folder Path
3. Install dependencies:
pip install -r requirements.txt
4. Run the app:
streamlit run resume_app.py

## Folder Structure
Edunet/
├── resume_app.py
├── requirements.txt
├── README.md
├── resumes/

## License
This project is for educational and demo purposes.
