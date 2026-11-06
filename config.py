import os
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("OPENAI_API_KEY","")
MODEL=os.getenv("OPENAI_MODEL","gpt-4o-mini")
ERP_URL=os.getenv("ERP_API_BASE_URL","http://127.0.0.1:8080").rstrip("/")
