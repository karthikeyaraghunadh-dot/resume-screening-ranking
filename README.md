# Resume Screening & Candidate Ranking System
Future Interns ML Task 3 (2026).

## Pipeline
Resume + Job Description → Cleaning → Skill Extraction → TF-IDF → Cosine Similarity → Skill Coverage → Weighted Score → Ranking.

## Score
60% semantic TF-IDF similarity + 40% required-skill coverage.

## Run
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.run_screening
streamlit run app.py
```

## Outputs
`reports/candidate_ranking.csv`

## Features
- TXT and PDF resume reading
- NLP preprocessing
- Skill extraction
- Job/resume similarity
- Missing-skill identification
- Candidate ranking
- Streamlit interface

Recommended dataset:
https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset

The included resumes are synthetic demo data for immediate testing. Do not publish private resumes without permission.
