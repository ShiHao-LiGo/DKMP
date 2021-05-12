from django.shortcuts import render
from django.http import HttpResponse
import re

# Create your views here.
from rabc.models import User, Permission


# Create your views here.
def login_view(request):
    return render(request, "login.html", None)


from django.shortcuts import render, HttpResponse, redirect
from rabc.models import User, Permission, Role
# Create your views here.
from rabc.service.permission import initial_permission


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(name=username, pwd=pwd).first()
        if user:
            # 验证身份
            request.session["user_id"] = user.pk
            request.session["username"] = username
            initial_permission(user, request)
            return render(request, "index.html")
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(name=username).first()
        if user and username != "":
            return render(request, "login.html", {'message': "用户名重复，换个名字试试"})
        elif not email:
            return render(request, "login.html", {'message': "邮箱重复，换个邮箱试试"})
        else:
            new = User(name=username, email=email, pwd=pwd)
            new.save()
            return render(request, "login.html", {'message': "注册成功,请登录"})
    return render(request, "login.html")


def user(request):
    # 获取session键值，如果不存在不报错，返回None
    permission_list = request.session.get('permission_list', [])
    # print(permission_list)
    path = request.path_info
    # print(path)
    flag = False
    for permission in permission_list:
        permission = "^%s$" % permission
        ret = re.match(permission, path)
        if ret:
            flag = True
            break
    # print(flag)
    if not flag:
        return HttpResponse('无访问权限！')
    return HttpResponse('查看用户')


def logout(request):
    request.session.clear()
    return render(request, "index.html")
