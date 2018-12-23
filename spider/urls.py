from django.conf.urls import url

from spider import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    url('show/', views.show, name='spider_show'),
]
