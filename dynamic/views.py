from django.contrib import auth
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from dynamic.forms import LoginForm
# Create your views here.
from dynamic.models import FileExcel, User


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
        form = LoginForm(request.POST or None)
        print(form.errors)
        # if form.is_valid():
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        result = User.objects.get(username=username)
        user = auth.authenticate(username=username, password=password)
        print(result)
        if result is not None:
            if not user:
                return HttpResponse("noactive")
            if user.is_active:
                auth.login(request, user)
                return HttpResponse("success")

        else:
            return HttpResponse("fail")
        # return HttpResponse("验证失败")
    else:
        return HttpResponse("method错误")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        result = User.objects.create_user(username=username, email=email, password=password)
        if result:
            return HttpResponse("success")
        else:
            return HttpResponse("fail")

    else:
        return HttpResponse("method错误")


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


def userinfo(req):
    return render(req, 'userinfo.html')


#
# def logout(req):
#     if req.user.is_authenticated:
#         del req.session['username']
#         return render(req, 'login_register.html')


def jihuo(req):
    return render(req, "jihuo.html")
