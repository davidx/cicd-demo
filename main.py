# main.py
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Fly.io demo app"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/api/time")
async def get_time():
    return {"time": datetime.now().isoformat()}