from fastapi import FastAPI
from multiprocessing import Process

app = FastAPI()

@app.get("/")
async def root():
    return {"health": "OK"}

def run_server():
    uvicorn.run(app)
    
def server():
    proce.Process(target=run_server, args=(), daemon=True)
    proc.start()