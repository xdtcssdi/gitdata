import hashlib
import os
import time

from django.http import HttpResponse
from django.shortcuts import render

# 首页
from dynamic.forms import UploadFileForm

# Create your views here.


def index(request):
    return render(request, "index.html")


def show_list(request):
    return render(request, "list.html")





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
    f = "\"http://127.0.0.1:8000/media/excels/example.csv\""

    return render(req, "bargraph.html", context={
        "data": f
    })
