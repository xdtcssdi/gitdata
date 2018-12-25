from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

import requests
from bs4 import BeautifulSoup

from spider.models import ImageItem


def show(request):
    if not request.user.is_authenticated:
        return redirect("/login_register")
    size = 16
    if request.GET.get('page'):
        page = int(request.GET['page'])
    else:
        page = 1

    p = Paginator(ImageItem.objects.all(), size)
    current = p.get_page(page)
    return render(request, "imageList.html", {"datas": current,
                                              "current_page": page,
                                              "page_num": range(page, page + 11),
                                              "hasLast": current.has_previous(),
                                              "hasNext": current.has_next()})


import sqlite3

if __name__ == '__main__':
    for i in range(1, 59):
        all_url = 'http://www.umei.cc/tupiandaquan/fengjingtupian/' + str(i) + '.htm'
        start_html = requests.get(all_url)
        start_html.encoding = 'utf8'
        Soup = BeautifulSoup(start_html.text, "lxml")
        urls = [url['src'] for url in Soup.find('div', class_='TypeList').find_all('img')]
        titles = [title.get_text() for title in Soup.find('div', class_='TypeList').find_all('span')]

        conn = sqlite3.connect('../db.sqlite3')
        c = conn.cursor()
        for item in zip(titles, urls):
            name_ = item[0]
            img_ = item[1]
            sql = "INSERT INTO spider_imageitem (mid,name,img) VALUES (null ,\'" + name_ + "\' , \'" + img_ + "\')"
            print(sql)
            c.execute(sql)
        conn.commit()
        conn.close()
