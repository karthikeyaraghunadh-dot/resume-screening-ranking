# Exact VS Code Setup
1. Open this folder in VS Code.
2. Terminal → New Terminal.
3. Run:
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
If PowerShell blocks activation, use Command Prompt:
```cmd
.venv\Scripts\activate.bat
```
4. Run screening (IMPORTANT: use module form):
```powershell
python -m src.run_screening
```
5. Launch website:
```powershell
streamlit run app.py
```
The project includes demo resumes, so it works immediately.
For final submission, replace demo data with appropriately licensed/anonymized resume data.
