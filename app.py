import json
import time
from scraper import fetch_price
from agent import agent_decide
from notifier import notify

URL = "PRODUCT_URL"
TARGET_PRICE = 70000

def load_last_price():
    with open("storage.json") as f:
        return json.load(f).get("last_price")

def save_price(price):
    with open("storage.json", "w") as f:
        json.dump({"last_price": price}, f)

def parse_sleep(text):
    if "30" in text: return 1800
    if "2" in text: return 7200
    if "6" in text: return 21600
    return 86400

while True:
    old_price = load_last_price()
    new_price = fetch_price(URL)

    decision = agent_decide(old_price, new_price, TARGET_PRICE)

    if decision["notify"] == "YES":
        notify(f"Price dropped to ₹{new_price}")

    save_price(new_price)

    sleep_time = parse_sleep(decision["next_check"])
    time.sleep(sleep_time)
