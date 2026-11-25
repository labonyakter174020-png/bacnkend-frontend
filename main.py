# ==========================================
# main.py  ->  The project starts from here
# Run:  uvicorn main:app --reload
# ==========================================
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from db import engine, base
from model import student, subjects   # importing models registers the tables
from routers import student_controller

# Create the tables in the database if they don't exist yet
base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management Project")

# CORS: lets the API work even if the HTML is opened from elsewhere (e.g. VS Code Live Server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_controller.router)

FRONTEND_FOLDER = Path(__file__).parent / "frontend"
app.mount("/", StaticFiles(directory=FRONTEND_FOLDER, html=True), name="frontend")
