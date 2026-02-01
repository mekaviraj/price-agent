import requests
from bs4 import BeautifulSoup

def fetch_price(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    # Example selector (adjust per site)
    price_text = soup.select_one(".price").text
    price = int(price_text.replace(",", "").replace("₹", "").strip())
    return price
