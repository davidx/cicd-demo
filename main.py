# main.py
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,  # Required by Jinja2Templates
            "message": "Welcome to the CICD Demo App from David",
            "timestamp": datetime.now().isoformat()
        }
    )

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/api/time")
async def get_time():
    return {"time": datetime.now().isoformat()}