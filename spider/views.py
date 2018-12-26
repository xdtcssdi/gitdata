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


