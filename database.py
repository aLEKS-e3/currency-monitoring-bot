from datetime import date
from sqlite3 import Connection

import pandas as pd


def manage_db(conn, cur, date, rate) -> None:
    cur.execute("CREATE TABLE IF NOT EXISTS rates(datetime, exchange_rate)")
    cur.execute("INSERT INTO rates VALUES(?, ?);", (date, rate))

    conn.commit()


def get_xlsx_file(conn: Connection, today: date) -> None:
    today_data = pd.read_sql_query(
        f"SELECT * FROM rates WHERE DATE(datetime) = '{today}'",
        conn
    )
    filename = f"{today}-usd-uah-rate.xlsx"
    today_data.to_excel(filename, index=False)
