import streamlit as st
from pathlib import Path
from src.screening import read_resume,screen_resume
st.set_page_config(page_title="Resume Screening AI",page_icon="📄",layout="wide")
st.title("📄 Resume Screening & Candidate Ranking System")
job=st.text_area("Job Description",Path("data/job_description.txt").read_text(encoding="utf8"),height=250)
uploads=st.file_uploader("Upload TXT/PDF resumes",type=["txt","pdf"],accept_multiple_files=True)
if uploads and job.strip():
    rows=[]; details={}
    for u in uploads:
        if u.name.lower().endswith(".pdf"):
            p=Path("data")/u.name; p.write_bytes(u.getbuffer()); text=read_resume(p); p.unlink(missing_ok=True)
        else: text=u.getvalue().decode("utf8",errors="ignore")
        r=screen_resume(text,job); details[u.name]=r
        rows.append({"Candidate":u.name,"Final Score":round(r["score"],2),"Similarity":round(r["similarity"],2),"Skill Coverage":round(r["coverage"],2),"Fit":r["fit"]})
    import pandas as pd
    df=pd.DataFrame(rows).sort_values("Final Score",ascending=False).reset_index(drop=True); df.insert(0,"Rank",range(1,len(df)+1))
    st.subheader("🏆 Candidate Ranking"); st.dataframe(df,use_container_width=True,hide_index=True)
    name=st.selectbox("Candidate details",df.Candidate)
    r=details[name]; c1,c2,c3=st.columns(3)
    c1.metric("Final Score",f"{r['score']:.1f}/100"); c2.metric("Similarity",f"{r['similarity']:.1f}%"); c3.metric("Skill Coverage",f"{r['coverage']:.1f}%")
    a,b=st.columns(2)
    a.success("Matched Skills: "+(", ".join(r["matched"]) or "None"))
    b.error("Missing Required Skills: "+(", ".join(r["missing"]) or "None"))
else: st.info("Enter a job description and upload at least one resume.")
st.caption("Decision-support prototype: human review is required; do not use protected or irrelevant personal attributes.")
