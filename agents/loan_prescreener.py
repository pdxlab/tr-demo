"""
Loan pre-screening agent (TR demo) — with safety guardrails.
"""
import os, re
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "sk-demo"))

SYSTEM_PROMPT = open("prompts/system_prompt.txt").read()

BIAS_INDICATORS = [
    r'\b(?:race|ethnicity|religion|gender|sex|national origin|age|disability)\b',
    r'\b(?:neighborhood|zip code|area|community|lifestyle)\b',
]

def _check_for_bias(text: str) -> list[str]:
    findings = []
    for pattern in BIAS_INDICATORS:
        if re.search(pattern, text, re.IGNORECASE):
            findings.append(pattern)
    return findings

def assess_applicant(profile: dict) -> dict:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Assess this applicant: {profile}"},
        ],
        temperature=0,
    )
    output = response.choices[0].message.content
    bias_flags = _check_for_bias(output)
    if bias_flags:
        return {"error": "Output flagged for potential bias", "flags": bias_flags}
    return {"recommendation": output, "model": "gpt-4", "safety_checked": True}
