from mysql.connector import connect
import logging
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

SITE = "INVESTING"
SITE_URL = "https://ru.investing.com/"



def set(param):
    try:
        with connect(
                    host="localhost",
                    user="root",
                    password="ander463",
                    database="news"
            ) as connection:
            query = """INSERT INTO news_tabel(text, url, site, time)
                VALUES(%s, %s, %s, %s)
                """
            data = []
            data.append(param)
            logging.info(data)
            with connection.cursor() as cursor:
                cursor.executemany(query, data)
                connection.commit()
                data.clear()

    except Exception as e:
        logging.error(e)

def get():
    try:
        with connect(
                    host="localhost",
                    user="root",
                    password="ander463",
                    database="news"
            ) as connection:
            with connection.cursor() as cursor:
                query = "SELECT * FROM news_tabel"
                cursor.execute(query)
                data_string = []
                for i in cursor.fetchall():
                    data_string.append(i[1])
                return data_string



    except Exception as e:
        logging.error(e)



def generate_news():
    data = []
    a = ["https://ru.investing.com/news/stock-market-news", "https://ru.investing.com/news/economy",
             "https://ru.investing.com/news/economic-indicators", "https://ru.investing.com/news/headlines",
             "https://ru.investing.com/news/forex-news"]
    for i in a:
        http = requests.get(str(i))
        if http:
            logging.info(i)
            page = BeautifulSoup(http.text, "html.parser")
            dad = page.findAll("a", class_="title")
            logging.info(dad)
            if dad:
                for d in dad:
                    if d:
                        data.append((d.text, SITE_URL + d.get("href"), SITE, datetime.now().strftime("%y-%B-%d: %H")))
    return data
