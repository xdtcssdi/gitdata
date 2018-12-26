import sqlite3

import requests
from bs4 import BeautifulSoup



def getSql():
    for i in range(1, 59):
        all_url = 'http://www.umei.cc/tupiandaquan/fengjingtupian/' + str(i) + '.htm'
        start_html = requests.get(all_url)
        start_html.encoding = 'utf8'
        Soup = BeautifulSoup(start_html.text, "lxml")

        urls = [url['src'] for url in Soup.find('div', class_='TypeList').find_all('img')]
        titles = [title.get_text() for title in Soup.find('div', class_='TypeList').find_all('span')]

        for item in zip(titles, urls):
            name_ = item[0]
            img_ = item[1]
            sql = "INSERT INTO spider_imageitem (mid,name,img) VALUES (null ,\'" + name_ + "\' , \'" + img_ + "\')"
            yield sql

        #     c.execute(sql)
        # conn.commit()
        # conn.close()


if __name__ == '__main__':
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    for sql in getSql():
        print(sql)
        c.execute(sql)
    conn.commit()
    conn.close()
