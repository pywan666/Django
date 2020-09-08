from datetime import date

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from booktest.models import BookInfo, video, user_database
from django.views.generic import View


# 首页显示图书信息
def index(request):
    books = BookInfo.objects.all()  # 1,查询所有图书信息
    return render(request, 'booktest/index.html', {'books': books})  # 2,使用模板


# 新增一本图书
def create(request):
    b = BookInfo()  # 1,创建BookInfo对象
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990, 12, 14)
    b.save()  # 2,保存进数据库
    return redirect('/index')  # 3,返回应答,让浏览器再访问/index,重定向


# 删除点击的图书
def delete(request, bid):
    book = BookInfo.objects.get(id=bid)  # 通过bid获取图书对象
    book.delete()  # 删除
    return redirect('/index')  # 重定向首页


# 视频主页
def video_index(request):
    if request.session.has_key('islogin'):
        islogin = 1
    else:
        islogin = 0
    # path = reverse('video_index')
    return render(request, 'booktest/video_index.html', {'islogin': islogin})


# 动漫列表
def video_(request, title_s, page):
    list_s = video.objects.filter(type=title_s)  # 获取type值为title_s的所有数据
    if len(list_s) != 0:
        max_list = (len(list_s) // 40) + 1  # 求获取到的(数据总数/20取整数+1)为html生成多少页做准备
        list_ = []
        title = ''
        max_page = 0
        if int(page) == max_list:  # 判断页数是否等于max_list
            max_page = int(len(list_s))
        else:
            max_page = int(page) * 40
        for x in range((int(page) - 1) * 40, max_page):
            list_.append(list_s[x])
        if title_s == 'comic_m3u8':
            title = '动漫-1'
        elif title_s == 'comic_mp4':
            title = '动漫-2'
        elif title_s == 'rihan':
            title = '日韩'
        elif title_s == 'domestic':
            title = '国产'
        elif title_s == 'oumei':
            title = '欧美'
        elif title_s == 'sanji':
            title = '三级'
        return render(request, 'booktest/video.html', {'list_': list_, 'title': title,
                                                       'title_s': title_s, 'page_': page, 'max_list': str(max_list)})
    else:
        return HttpResponse('空')


def video_play(request, id_s):
    id_objects = video.objects.get(id=id_s)
    if id_objects.type == 'comic_m3u8':
        return render(request, 'booktest/video_m3u8.html', {'video': id_objects.video, 'title': id_objects.name})
    else:
        return render(request, 'booktest/video_mp4.html', {'video': id_objects.video,
                                                           'title': id_objects.name, 'img': id_objects.img})


# 定义类视图 登录
class Login_register(View):
    def get(self, request):
        user = request.COOKIES.get('username')
        password = ''
        remember = ''
        if request.COOKIES.get('remember') == '1':
            password = request.COOKIES.get('password')
            remember = request.COOKIES.get('remember')
        return render(request, 'booktest/login.html', {'user': user, 'password': password, 'remember': remember})

    def post(self, request):
        button = request.POST.get('button')
        if button == '登录':
            # 1.获取用户名密码
            user = request.POST.get('username')  # request中保存着所有提交的数据，获取用户名
            password = request.POST.get('password')  # 获取密码
            remember = request.POST.get('remember')  # 是否记住密码
            # 2.校验账号密码
            if user_database.objects.filter(user=user):  # filter如果数据不存在返回为空，get如果数据不存在则抛异常
                if user_database.objects.filter(password=password):
                    Response = JsonResponse({'res': 66})  # 成功登录
                    Response.set_cookie('username', user)
                    if remember == 'true':
                        Response.set_cookie('password', password)
                        Response.set_cookie('remember', '1')
                    return Response
                else:
                    return JsonResponse({'res': 101})  # 用户密码错误
            else:
                return JsonResponse({'res': 100})  # 用户不存在


# get提交
def get_request(request):
    # 获取request中提交的参数
    data = request.GET
    # 获取一键一值方法
    name = data['name']
    name_1 = data.get('name')
    # 获取一键多值方法
    pass_ = data.getlist('pass')
    # print(name, name_1, pass_)
    return HttpResponse('ok')


# 设置cookie
def set_cookie(request):
    Response = HttpResponse('get_cookie')
    if request.COOKIES.get('name') is None:  # 用于判断是否存在cookie
        Response.set_cookie('name', 'admin', max_age=60)
        Response.set_cookie('pass_w', '123', max_age=60)
    return Response


# 获取cookie
def get_cookie(request):
    cookie = request.COOKIES
    name = cookie.get('name')
    pass_w = cookie.get('pass_w')
    print(name, pass_w)
    return HttpResponse('get_cookie')
