import hashlib
import os
import time

from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
# 首页
from dynamic.forms import UploadFileForm

# Create your views here.
from dynamic.models import FileExcel


def index(request):
    return render(request, "index.html")


def show_list(request):
    size = 10
    if request.GET.get('page'):
        page = request.GET['page']
    else:
        page = 1

    p = Paginator(FileExcel.objects.all(), size)
    current = p.get_page(page)
    return render(request, "list.html", {"datas": current,
                                         "current_page":page,
                                         "page_num": p.num_pages*[0],
                                         "hasLast": current.has_previous(),
                                         "hasNext": current.has_next()})


def upload(request):
    if request.method == 'POST':  # 获取对象
        # form = UploadFileForm(request.POST, request.FILES)
        form = UploadFileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

            return HttpResponse('OK')
        else:
            return HttpResponse("Valid fail")

    return render(request, 'upload.html')


def show(req):
    if req.method == 'GET':
        name = req.GET.get('name')
        url = "\"http://127.0.0.1:8000/media/excels/"+name+"\""

        return render(req, "bargraph.html", context={
            "data": url
        })
