import subprocess
import json

def agent_decide(old_price, new_price, target_price):
    prompt = f"""
Old price: {old_price}
New price: {new_price}
Target price: {target_price}

Tasks:
1. Should the user be notified? (YES or NO)
2. When should the price be checked again?
Choose one: 30 min, 2 hours, 6 hours, 24 hours

Respond ONLY in JSON.
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return json.loads(result.stdout)
