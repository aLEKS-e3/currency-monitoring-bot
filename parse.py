import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")


def parse_usd_to_uah_rate() -> str:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    rate = soup.select_one(
        "div > div > div > div:nth-child(1) > div > span > div > div"
    ).text

    return rate
