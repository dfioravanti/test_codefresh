from typing import Optional

from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def read_file():
    with open('data') as f:
        lines = f.readline()
    return Response(content=lines)

@app.post("/{content}")
def write_file(content: str):
    with open('data', 'w') as f:
        lines = f.write(content)
    

