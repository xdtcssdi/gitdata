from django.contrib import auth
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from celery_tasks.task import send_msg
from dynamic.forms import LoginForm
# Create your views here.
from dynamic.models import FileExcel, User, CheckCode


def index(request):
    return render(request, "index.html")


def show_list(request):
    if not request.user.is_authenticated:
        return redirect("/login_register")
    size = 10
    if request.GET.get('page'):
        page = request.GET['page']
    else:
        page = 1

    p = Paginator(FileExcel.objects.order_by('-uploadtime').all(), size)
    current = p.get_page(page)
    return render(request, "list.html", {"datas": current,
                                         "current_page": page,
                                         "page_num": p.num_pages * [0],
                                         "hasLast": current.has_previous(),
                                         "hasNext": current.has_next()})


def upload(request):
    if not request.user.is_authenticated:
        return redirect("/login_register")
    if request.method == 'POST':  # 获取对象
        f = FileExcel(user=request.user, describle=request.POST['describle'],
                      excel=request.FILES["excel"],
                      pname=request.POST['pname'])

        f.save()

        return redirect("list")

    return render(request, 'upload.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        result = User.objects.filter(username=username)
        if not result:
            return HttpResponse("nofound")
        elif not result[0].is_active:
            return HttpResponse("noactive")

        user = auth.authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth.login(request, user)
                return HttpResponse("success")
        else:
            return HttpResponse("fail")

    else:
        return HttpResponse("method错误")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        res = User.objects.filter(username=username)
        if res:
            return HttpResponse("nounique")
        result = User.objects.create_user(username=username, email=email, password=password)

        if result:
            result.is_active = False
            result.save()
            randomCode = get_random_str()
            CheckCode.objects.create(user=result, code=randomCode)
            send_msg(email, randomCode)
            # send_mail('验证您的用户信息', '您已经注册账户成功，现在需要您访问如下链接：http://localhost:8000/check?code=' + randomCode,
            #           settings.DEFAULT_FROM_EMAIL, [email],
            #           fail_silently=False)
            return HttpResponse("success")
        else:
            return HttpResponse("fail")

    else:
        return HttpResponse("method错误")


import uuid
import hashlib


def get_random_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()


def show(req):
    if req.method == 'GET':
        name = req.GET.get('name')
        url = "\"http://127.0.0.1:8000/media/excels/" + name + "\""

        return render(req, "bargraph.html", context={
            "data": url
        })


def login_register(req):
    if req.user.is_authenticated:
        return redirect("/")
    lf = LoginForm()
    # rf = RegisterForm()
    return render(req, "login_register.html", {'lf': lf})


def userinfo(request):
    size = 10
    if request.POST.get('page'):
        page = request.POST['page']
    else:
        page = 1

    p = Paginator(FileExcel.objects.filter(user=request.user).order_by('-uploadtime').all(), size)
    current = p.get_page(page)
    return render(request, "userinfo.html", {'user': request.user, "datas": current,
                                             "current_page": page,
                                             "page_num": p.num_pages * [0],
                                             "hasLast": current.has_previous(),
                                             "hasNext": current.has_next()})


def modfiyuserinfo(req):
    if req.method == 'POST':
        newname = req.POST.get('username')
        password = req.POST.get('password')
        newpassword = req.POST.get('newpassword')
        newemail = req.POST.get('email')
        print(newname)
        user = auth.authenticate(username=req.user.username, password=password)
        if user:
            user.username = newname
            user.set_password(newpassword)
            user.email = newemail
            user.save()
            auth.login(req, user=user)
            return HttpResponse("success")
        return HttpResponse("fail")


def logout(req):
    if req.user.is_authenticated:
        auth.logout(req)
        return redirect("login_register")


def check(request):
    code = request.GET['code']
    cc = CheckCode.objects.get(code=code)

    if cc:
        cc.user.is_active = True
        cc.user.save()
        cc.delete()
    else:
        return HttpResponse("验证失败")
    return HttpResponse("成功")
