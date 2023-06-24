from django.shortcuts import render, HttpResponse

# Create your views here.
# URL 与函数的对应关系


def index(request):
    return HttpResponse("欢迎使用")


def users(request):
    return HttpResponse("用户页面")

def usersadd(request):
    #return HttpResponse("用户添加")
    # 会去 app01 templates 目录下找user_add.html文件（根据app的注册顺序逐一找，从第一个app开始，然后app2）
    return render(request, "user_add.html")