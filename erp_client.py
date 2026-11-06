import requests
from .config import ERP_URL
def get(path,params=None):
    r=requests.get(ERP_URL+path,params=params,timeout=15)
    r.raise_for_status()
    return r.json()
