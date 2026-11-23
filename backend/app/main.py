from fastapi import FastAPI
from app.api import auth_router

app = FastAPI(title="Inventory Movement Tracker")

app.include_router(auth_router)