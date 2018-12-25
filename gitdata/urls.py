"""gitdata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url
from django.urls import path, include
from django.views.static import serve

from dynamic import views
from gitdata import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    url('^$', views.index, name='index'),
    url('upload/', views.upload),
    url(r'^show/', views.show),
    url('list/', views.show_list, name='list'),
    url('login/', views.login, name='login'),
    url('login_register/', views.login_register, name='login_register'),
    url('register/', views.register, name='register'),
    url('spider/', include("spider.urls"), name='spider'),
    url('check/', views.check, name='check'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^userinfo', views.userinfo, name='userinfo'),
    url(r'^modfiyuserinfo', views.modfiyuserinfo, name='modfiyuserinfo'),
    url(r'logout', views.logout, name='logout')
]
