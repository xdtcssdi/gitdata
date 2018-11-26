from django.contrib import auth
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from dynamic.forms import UploadFileForm, LoginForm
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

    p = Paginator(FileExcel.objects.all(), size)
    current = p.get_page(page)
    return render(request, "list.html", {"datas": current,
                                         "current_page": page,
                                         "page_num": p.num_pages * [0],
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


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        print(form.errors)
        # if form.is_valid():
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
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

        result = User.objects.create_user(username=username,email=email,password=password);

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
