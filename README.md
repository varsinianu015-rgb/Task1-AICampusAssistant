# College AI Assistant – Python ERP version

This version replaces Java/Spring Boot with a Python FastAPI ERP service.

## Run on Windows

Install Python 3.11+, open CMD in this folder:

```cmd
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Add your OpenAI API key to `.env`. Never share screenshots showing the key.

Open three terminals in this folder (activate `.venv` in each):

Terminal 1 – ERP API:
```cmd
uvicorn erp_service.main:app --reload --port 8080
```
Open http://127.0.0.1:8080/docs

Terminal 2 – AI API:
```cmd
uvicorn ai_assistant.main:app --reload --port 8000
```

Terminal 3 – UI:
```cmd
streamlit run streamlit_app.py
```
Open the Streamlit URL, normally http://localhost:8501.

SQLite database and fictional demo records are created automatically. For MySQL, install `pymysql` and set `DATABASE_URL=mysql+pymysql://user:password@localhost:3306/college_erp` in `.env`.

ERP endpoints: `/api/students/count`, `/api/students/{student_id}`, `/api/students?department=...`, `/api/staff?department=...`, `/api/staff/class-teacher?department=...`, `/api/attendance/report`.

Demo data is fictional. This starter has no production authentication; add authorization and audit logging before using real student/staff records.
