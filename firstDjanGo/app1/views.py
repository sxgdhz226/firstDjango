from app1 import models
from django.shortcuts import HttpResponse, render, redirect
# 展示出版社列表
def publisher_list(request):
    # 去数据库查出所有的出版社,填充到HTML中,给用户返回
    ret = models.Publisher.objects.all().order_by("id")
    return render(request, "publisher_list.html", {"publisher_list": ret})