from django.db import models


# Create your models here.

class BookInfoManagr(models.Manager):  # 自定义管理器类
    def all(self):  # 重写all()函数
        books = super().all()  # 1，调用父类的all(),获取所有数据
        books = books.filter(isDelete=False)  # 2,对数据进行过滤
        return books  # 3,返回books

    def create_book(self, btitle, bpub_date):  # 封装函数，添加数据到表中(删增改查)
        model_class = self.model  # 获取调用这个管理类的类名
        book = model_class()  # 1，创建一个图书对象
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()  # 2,保存进数据库里
        return book  # 3,返回book


# 图书一类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)  # 图书名字 CharFileld说明是一个字符串，max_length指定字符串的最大长度
    bpub_date = models.DateField()  # 出版日期 DateField说明是一个日期类型
    bread = models.IntegerField(default=0)  # 阅读量 IntegerField说明是一个整数字段
    bcomment = models.IntegerField(default=0)  # 评论量  IntegerField说明是一个整数字段
    isDelete = models.BooleanField(default=False)  # 删除标记 BooleanField说明是个bool类型
    objects = BookInfoManagr()

    def __str__(self):
        return self.btitle  # 英雄名字


# 英雄多类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)  # 英雄名字
    hgender = models.BooleanField(default=False)  # 性别
    hcomment = models.CharField(max_length=200)  # 备注
    # 关系属性 hbook,建立图书类和英雄类之间的一对多关系
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)  # 删除标记

    def __str__(self):
        return self.hname  # 英雄名字


class video(models.Model):  # 视频数据库
    type = models.CharField(max_length=200)  # 类别
    name = models.CharField(max_length=200)  # 名字
    img = models.CharField(max_length=200)  # 图片
    video = models.CharField(max_length=200)  # 地址
    remarks = models.CharField(max_length=200)  # 备注

    class Meta:  # 让模型对应的数据库不依赖于应用名字
        db_table = 'video'  # 指定模型对应的表明


class user_database(models.Model):  # 用户数据库
    user = models.CharField(max_length=128)  # 用户名
    password = models.CharField(max_length=128)  # 密码
    registration_time = models.DateField(auto_now_add=True)  # 注册时间
    modify_time = models.DateField(auto_now=True)  # 最后修改时间

    class Meta:  # 让模型对应的数据库不依赖于应用名字
        db_table = 'user_database'  # 指定模型对应的表明

