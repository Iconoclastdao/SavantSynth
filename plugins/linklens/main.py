from flask import Flask, request, jsonify
from utils.claim_extractor import ClaimExtractor
from config import MODEL_NAME
import hashlib
import subprocess
import os

app = Flask(__name__)
extractor = ClaimExtractor(MODEL_NAME)

@app.route('/scan', methods=['POST'])
def scan_claims():
    data = request.json
    claims = extractor.extract_claims(data['text'])
    hashed_claims = [hashlib.sha256(c.encode()).hexdigest() for c in claims]
    return jsonify({"claims": claims, "hashes": hashed_claims})

@app.route('/zk_proof', methods=['POST'])
def zk_proof():
    claim_hash = request.json['hash']
    input_file = os.path.join("zk", "input.json")
    with open(input_file, "w") as f:
        f.write(f'{{"claimHash":"{claim_hash}"}}')
    subprocess.run(["bash", "zk/build_zk.sh"])
    return jsonify({"status": "zk_proof_generated"})
