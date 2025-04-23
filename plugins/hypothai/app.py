from fastapi import FastAPI
from hypothai import generate_hypothesis_router

app = FastAPI(title="HypothAI Plugin")

app.include_router(generate_hypothesis_router, prefix="/generate")