from flask import Flask, request, jsonify
from utils.format_utils import format_proposal
from services.onchain_connector import submit_proposal
from ai.proposal_ranker import rank_proposal

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def propose():
    data = request.json
    proposal = format_proposal(data["title"], data["rationale"], data["actions"])
    score = rank_proposal(proposal, data["context"])
    tx = submit_proposal(proposal)
    return jsonify({"proposal": proposal, "ai_score": score, "tx_hash": tx})