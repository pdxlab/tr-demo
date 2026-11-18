"""
Loan pre-screening agent (TR demo).
Accepts applicant profile, queries an LLM to produce a preliminary
recommendation. Intentionally simplified for demo purposes.
"""
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "sk-demo"))

SYSTEM_PROMPT = """You are a loan pre-screening assistant for a financial institution.
Given an applicant profile, assess their preliminary eligibility for a personal loan.
Be objective and base your assessment solely on financial data provided.
Do not consider race, gender, religion, national origin, or other protected characteristics."""

def assess_applicant(profile: dict) -> dict:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Assess this applicant: {profile}"},
        ],
        temperature=0,
    )
    return {"recommendation": response.choices[0].message.content, "model": "gpt-4"}
