
from fastapi import FastAPI
import requests 

app = FastAPI()


@app.get("/")
def read_root():
    r = requests.get('http://myserver:9999/')
    r = r.json()
    return r

