from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict
import random

generate_hypothesis_router = APIRouter()

class GraphInput(BaseModel):
    nodes: List[Dict]
    edges: List[Dict]

class HypothesisOutput(BaseModel):
    hypotheses: List[str]

@generate_hypothesis_router.post("/hypotheses", response_model=HypothesisOutput)
def generate_hypotheses(graph: GraphInput):
    hypotheses = []
    for edge in graph.edges:
        src_label = next((n["label"] for n in graph.nodes if n["id"] == edge["source"]), "")
        tgt_label = next((n["label"] for n in graph.nodes if n["id"] == edge["target"]), "")
        hypotheses.append(
            f"Investigate whether {src_label} influences or regulates {tgt_label}."
        )
    # Add creative augmentations
    if len(hypotheses) > 2:
        hypotheses.append("Consider latent variables that may link multiple observed interactions.")
        hypotheses.append("Model downstream effects of modifying central nodes.")
    return HypothesisOutput(hypotheses=hypotheses)