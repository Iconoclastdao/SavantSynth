from fastapi import APIRouter
from pydantic import BaseModel
import spacy
import networkx as nx
import uuid
from typing import List, Dict

parse_paper_endpoint = APIRouter()
nlp = spacy.load("en_core_sci_sm")

class InputText(BaseModel):
    text: str

class GraphResponse(BaseModel):
    nodes: List[Dict]
    edges: List[Dict]
    rdf: str
    graphJSON: Dict

@parse_paper_endpoint.post("/paper", response_model=GraphResponse)
def parse_paper(data: InputText):
    doc = nlp(data.text)
    nodes = []
    edges = []
    G = nx.DiGraph()

    for ent in doc.ents:
        node_id = str(uuid.uuid4())[:8]
        G.add_node(node_id, label=ent.text, type=ent.label_)
        nodes.append({ "id": node_id, "label": ent.text })

    for i in range(len(doc.ents)-1):
        src = nodes[i]["id"]
        tgt = nodes[i+1]["id"]
        relation = "related_to"
        G.add_edge(src, tgt, relation=relation)
        edges.append({ "source": src, "target": tgt, "relation": relation })

    graph_json = nx.node_link_data(G)
    rdf_output = f"<rdf><graph nodes={len(nodes)} edges={len(edges)} /></rdf>"

    return GraphResponse(
        nodes=nodes,
        edges=edges,
        rdf=rdf_output,
        graphJSON=graph_json
    )