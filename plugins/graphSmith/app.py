from fastapi import FastAPI
from graphsmith import parse_paper_endpoint

app = FastAPI(title="GraphSmith Plugin")

app.include_router(parse_paper_endpoint, prefix="/parse")