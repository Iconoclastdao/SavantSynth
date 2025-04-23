import openai
from config import OPENAI_KEY, GPT_MODEL

openai.api_key = OPENAI_KEY

def generate_hypothesis(claim, context_matches):
    prompt = f"""Scientific Claim: {claim}
Known Concepts: {', '.join(context_matches)}

Suggest a novel hypothesis or experiment that logically extends this claim:"""
    
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()