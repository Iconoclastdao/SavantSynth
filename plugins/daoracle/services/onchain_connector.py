from web3 import Web3
from config import INFURA_URL, PRIVATE_KEY, DAO_CONTRACT
import json

w3 = Web3(Web3.HTTPProvider(INFURA_URL))
account = w3.eth.account.from_key(PRIVATE_KEY)

with open("contracts/ProposalFactory.abi.json") as f:
    abi = json.load(f)

dao = w3.eth.contract(address=DAO_CONTRACT, abi=abi)

def submit_proposal(description):
    txn = dao.functions.createProposal(description).build_transaction({
        "from": account.address,
        "nonce": w3.eth.get_transaction_count(account.address),
        "gas": 300000
    })
    signed_txn = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return w3.toHex(tx_hash)