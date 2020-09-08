"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, re_path

from booktest import views

# 直接访问应用里views的模板
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),  # 包含booktest应用的urls文件
    path('create/', views.create),  # 首页新增模板
    re_path(r'delete(\d+)/', views.delete),  # 首页列表删除模板

    path('', views.video_index, name='video_index'),  # 主页
    re_path(r"video_play/(.*?)/", views.video_play),  # 视频播放
    re_path(r"video/(?P<title_s>.*?)/(?P<page>.*?)/", views.video_),  # 视频列表 通过关键字参数获取值?P<关键字>

    # 使用类视图方式
    path('login/', views.Login_register.as_view()),  # ajax登录页面,登录、注册提交

    path('get/', views.get_request),  # get请求

    path('set_cookie/', views.set_cookie),  # set_cookie请求
    path('get_cookie/', views.get_cookie),  # get_cookie请求
]

