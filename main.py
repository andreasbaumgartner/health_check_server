from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"health": "OK"}


def run_server():
    uvicorn.run(app)

    
def server():
    proc.Process(target=run_server, args=(), daemon=True)
    proc.start()