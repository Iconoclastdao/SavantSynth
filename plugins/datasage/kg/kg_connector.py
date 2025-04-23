import rdflib
import networkx as nx

class KnowledgeGraph:
    def __init__(self, path):
        self.graph = rdflib.Graph()
        self.graph.load(path)

    def match_claim(self, claim_text):
        # Dumb match (improve with embedding model)
        matches = [str(s) for s in self.graph.subjects() if str(s).lower() in claim_text.lower()]
        return matches