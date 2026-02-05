import subprocess
import json
import re

def agent_decide(old_price, new_price, target_price):
    prompt = f"""
Old price: {old_price}
New price: {new_price}
Target price: {target_price}

Answer ONLY in this exact JSON format:
{{"notify":"YES or NO","next_check":"30 min | 2 hours | 6 hours | 24 hours"}}
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="ignore",
        capture_output=True
    )

    raw = result.stdout.strip()

    # Extract JSON safely
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not match:
        return {"notify": "NO", "next_check": "6 hours"}

    return json.loads(match.group())
