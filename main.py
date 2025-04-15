# main.py
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_iso_timestamp():
    """Return current timestamp in ISO format."""
    return datetime.now().isoformat()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Render the main page."""
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,  # Required by Jinja2Templates
            "message": "Welcome to the CICD Demo App from David",
            "timestamp": get_iso_timestamp()
        }
    )
@app.get("/health")
async def health():
    """Return service health status with timestamp."""
    return {
        "status": "ok",
        "timestamp": get_iso_timestamp()
    }

@app.get("/api/time")
async def get_time():
    return {"time": get_iso_timestamp()}