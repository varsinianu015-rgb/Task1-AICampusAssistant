from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
import requests
from .agent import answer_question
from .config import ERP_URL
app=FastAPI(title='College AI Assistant API')
class ChatRequest(BaseModel):
    question:str=Field(min_length=2,max_length=1000)
@app.get('/health')
def health():
    try: ok=requests.get(ERP_URL+'/health',timeout=3).ok
    except requests.RequestException: ok=False
    return {'status':'ok','erp_available':ok,'erp_url':ERP_URL}
@app.post('/chat')
def chat(body:ChatRequest):
    try:
        answer,tools=answer_question(body.question)
        return {'answer':answer,'tools_used':tools}
    except Exception as e: raise HTTPException(502,detail=str(e))
