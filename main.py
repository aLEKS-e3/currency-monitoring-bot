import asyncio
import logging
import os
import time
import schedule
import sqlite3
import sys
from datetime import datetime

from database import manage_db, get_xlsx_file
from parse import parse_usd_to_uah_rate
from telegram import main
from dotenv import load_dotenv


load_dotenv()

URL_TO_PARSE = os.getenv("URL")


def gather_data() -> None:
    date = datetime.now()
    rate = parse_usd_to_uah_rate(URL_TO_PARSE)

    with sqlite3.connect("usd-to-uah-rates.db") as conn:
        cur = conn.cursor()

        manage_db(conn, cur, date, rate)
        get_xlsx_file(conn, date.date())

        cur.close()


def launch() -> None:
    schedule.every().hour.do(gather_data)

    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    gather_data()
    asyncio.run(main())

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    launch()
