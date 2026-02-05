import requests
from bs4 import BeautifulSoup
import re

def fetch_price(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    price_text = soup.select_one(".price_color").text

    # extract only numbers and dot
    number = re.findall(r"\d+\.\d+", price_text)[0]
    return float(number)
