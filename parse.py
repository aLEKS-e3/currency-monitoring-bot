import requests
from bs4 import BeautifulSoup


def parse_usd_to_uah_rate(url: str) -> str:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    rate = soup.select_one(
        "div > div > div > div:nth-child(1) > div > span > div > div"
    ).text

    return rate
