import openai
from config import GPT_MODEL, OPENAI_KEY

openai.api_key = OPENAI_KEY

def rank_proposal(proposal_text, context):
    prompt = f"""
Given the following scientific context: {context}
Evaluate and rank the following DAO proposal for potential impact and scientific validity.

Proposal:
{proposal_text}

Respond with a score (0-10) and a 1-sentence justification.
"""
    res = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content.strip()