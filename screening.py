import re
from pathlib import Path
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS={"python","machine learning","scikit-learn","pandas","numpy","sql","nlp","git","statistics","tensorflow","pytorch","deep learning","docker","aws","fastapi","spacy","nltk","excel","power bi","java","javascript","react","node.js","mongodb","kubernetes","rest api","linux","data visualization","matplotlib"}

def clean_text(text):
    return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9+#.\-\s]"," ",str(text).lower())).strip()

def read_resume(path):
    p=Path(path)
    if p.suffix.lower()==".pdf":
        return "\n".join((x.extract_text() or "") for x in PdfReader(str(p)).pages)
    return p.read_text(encoding="utf8",errors="ignore")

def extract_skills(text):
    t=clean_text(text); found=[]
    for s in sorted(SKILLS,key=len,reverse=True):
        if re.search(r"(?<!\w)"+re.escape(s)+r"(?!\w)",t): found.append(s)
    return sorted(set(found))

def screen_resume(resume,job):
    js=set(extract_skills(job)); rs=set(extract_skills(resume))
    matched=sorted(js&rs); missing=sorted(js-rs)
    vec=TfidfVectorizer(ngram_range=(1,2),stop_words="english")
    m=vec.fit_transform([clean_text(job),clean_text(resume)])
    sim=float(cosine_similarity(m[0:1],m[1:2])[0][0])
    coverage=len(matched)/len(js) if js else 0
    score=(.60*sim+.40*coverage)*100
    fit="Excellent Fit" if score>=75 else "Good Fit" if score>=55 else "Moderate Fit" if score>=35 else "Low Fit"
    return {"score":score,"similarity":sim*100,"coverage":coverage*100,"fit":fit,"matched":matched,"missing":missing}
