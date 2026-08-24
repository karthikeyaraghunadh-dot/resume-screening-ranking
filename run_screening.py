from pathlib import Path
import pandas as pd
from src.screening import read_resume,screen_resume
def main():
    job=Path("data/job_description.txt").read_text(encoding="utf8")
    out=[]
    for p in list(Path("data/resumes").glob("*.txt"))+list(Path("data/resumes").glob("*.pdf")):
        r=screen_resume(read_resume(p),job)
        out.append({"Candidate":p.stem.replace("_"," "),"Final Score":round(r["score"],2),"Similarity":round(r["similarity"],2),"Skill Coverage":round(r["coverage"],2),"Fit":r["fit"],"Matched Skills":", ".join(r["matched"]),"Missing Skills":", ".join(r["missing"])})
    df=pd.DataFrame(out).sort_values("Final Score",ascending=False).reset_index(drop=True); df.insert(0,"Rank",range(1,len(df)+1))
    Path("reports").mkdir(exist_ok=True); df.to_csv("reports/candidate_ranking.csv",index=False)
    print(df[["Rank","Candidate","Final Score","Fit"]].to_string(index=False))
    print("\nSaved: reports/candidate_ranking.csv")
if __name__=="__main__": main()
