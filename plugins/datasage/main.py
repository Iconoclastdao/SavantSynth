from flask import Flask, request, jsonify
from utils.paper_parser import extract_claims
from kg.kg_connector import KnowledgeGraph
from gpt.hypothesis_gen import generate_hypothesis
from config import KG_PATH

app = Flask(__name__)
kg = KnowledgeGraph(KG_PATH)

@app.route("/analyze", methods=["POST"])
def analyze_paper():
    text = request.json["text"]
    claims = extract_claims(text)
    results = []

    for claim in claims:
        context = kg.match_claim(claim)
        hypothesis = generate_hypothesis(claim, context)
        results.append({"claim": claim, "matched_concepts": context, "hypothesis": hypothesis})

    return jsonify(results)