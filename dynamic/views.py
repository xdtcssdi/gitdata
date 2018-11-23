import hashlib
import os
import time

from django.http import HttpResponse
from django.shortcuts import render

# 首页
from gitdata.settings import BASE_DIR


# Create your views here.


def index(request):
    return render(request, "index.html")


def upload(request):
    if request.method == 'POST':  # 获取对象
        obj = request.FILES.get('project_file')
        # print(obj.name)
        t = time.time()

        data = obj.name + str(int(round(t * 1000)))

        tt = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()

        name = str(tt)[:20] + '.' + obj.name.split('.')[-1]

        f = open(os.path.join(BASE_DIR, 'media', 'excels', name), 'wb')

        for chunk in obj.chunks():
            f.write(chunk)

        f.close()
        return HttpResponse('OK')

    return render(request, 'upload.html')


def test(req):
    return render(req, "test.html")


def show(req):
    f = "\"http://127.0.0.1:8000/media/excels/example.csv\""

    return render(req, "bargraph.html", context={
        "data": f
    })
