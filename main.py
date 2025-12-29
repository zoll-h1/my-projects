from fastapi import FastAPI 

app = FastAPI(title="LifeOS API", version="0.1.0")
@app.get("/")
async def read_root():
    return {"system": "LifeOS", "status": "active", "version": "0.1.0"}
@app.get("/ping")
async def pong():
    return {"message": "pong"}