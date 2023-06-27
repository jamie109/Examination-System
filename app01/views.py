from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from app01.models import StuInfo, TeacherInfo, Exam, QuestionOption
# Create your views here.
# URL 与函数的对应关系


def index(request):
    return render(request, "index.html")#HttpResponse("欢迎使用")


def user(request):
    stu_list = StuInfo.objects.all()

    return render(request, "user.html", {"stu_list":stu_list})


def tpl(request):
    name = "wjm"
    roles = ["gu案例元", "vfaigg"]
    user_info = {"1":"aaa", "2":"bbbb"}
    return render(request, "tpl.html", {"n1":name,"n2":roles, "n3":user_info})

def news(request):
    # request内部封装了用户请求发出的数据
    # 1、获取请求方法 GET POST
    print(request.method)
    # 2、请求发来的值 /sth/？n1=12345&n2=999
    print(request.GET)
    # 3、在请求体中提交数据
    print(request.POST)
    # [响应]将字符串返回
    #return HttpResponse("用户页面")
    # [响应]重定向到其他页面
    return redirect("https://www.baidu.com")
    # [响应]将页面返回，读取html内容，渲染，替换---返回给用户浏览器
    #return render(request, "news.html")


def orm(request):
    # 操作表中数据
    ####### 1 新增
    # StuInfo.objects.create(username='s002', stuid='002', password='s002')
    # StuInfo.objects.create(username='s003', stuid='003', password='s003')
    # StuInfo.objects.create(username='s004', stuid='004', password='s004')
    # StuInfo.objects.create(username='s005', stuid='005', password='s005')
    # StuInfo.objects.create(username='s006', stuid='006', password='s006')
    # TeacherInfo.objects.create(teacherid='t001', password='t001')
    # TeacherInfo.objects.create(teacherid='t002', password='t002')
    # TeacherInfo.objects.create(teacherid='t003', password='t003')
    ####### 2 删除
    # TeacherInfo.objects.filter(teacherid='t001').delete()
    ####### 3 获取数据
    # data_list = TeacherInfo.objects.all()
    # #data_list = TeacherInfo.objects.filter(id=1)#也可以筛选
    # for obj in data_list:
    #     print(obj.teacherid, obj.password)
    ####### 4 更新数据
    #StuInfo.objects.filter(username='s001').update(stuid = '1')

    return HttpResponse("success!!!")
##################################################################################################
############################################# start ##############################################
##################################################################################################
def stuinfo(request):
    # 数据库中获取学生列表
    stu_list = StuInfo.objects.all()

    return render(request, "stuinfo.html", {"stu_list": stu_list})

def stuadd(request):
    """  添加学生信息  """
    #return HttpResponse("用户添加")
    # 会去 app01 templates 目录下找user_add.html文件（根据app的注册顺序逐一找，从第一个app开始，然后app2）
    if request.method == "GET":
        return render(request, "stu_add.html")
    # 获取用户提交的数据
    studentname = request.POST.get("studentname")
    studentid = request.POST.get("studentid")
    school = request.POST.get("school")
    pwd = request.POST.get("pwd")
    print(studentname,studentid,school,pwd)
    # score = request.POST.get("score")
    # 添加到数据库
    StuInfo.objects.create(stuname=studentname, stuid=studentid, stuschool=school, password=pwd)
    # 添加成功自动跳转
    return redirect("http://127.0.0.1:8000/stuinfo/")

def studelete(request):
    """删除学生"""
    stu_id = request.GET.get('stuid')
    StuInfo.objects.filter(id=stu_id).delete()
    return redirect("http://127.0.0.1:8000/stuinfo/")

def stuedit(request, stuid):
    """编辑学生信息"""
    if request.method == "GET":
        stu_obj = StuInfo.objects.filter(id=stuid).first()
        #print(stu_obj)
        # oldname = stu_obj.stuname
        # oldid = stu_obj.stuid
        # oldschool = stu_obj.stuschool
        # oldpwd = stu_obj.password
        return render(request, "stu_edit.html", {"stu_obj": stu_obj})

    # 获取管理员修改后的数据
    studentname = request.POST.get("studentname")
    studentid = request.POST.get("studentid")
    school = request.POST.get("school")
    pwd = request.POST.get("pwd")
    StuInfo.objects.filter(id=stuid).update(stuname=studentname, stuid=studentid, stuschool=school, password=pwd)
    # 修改成功自动跳转
    return redirect("http://127.0.0.1:8000/stuinfo/")

def stusearch(request):
    searchname = request.GET.get("searchname")
    print(searchname)
    stu_obj_search = StuInfo.objects.filter(stuname=searchname)#.first()
    #print(stu_obj_search)
    return render(request, "stu_search.html", {"searchobj":stu_obj_search})

# def stusearchres(request, searchname):
#     return render(request, "stu_search.html")

def teainfo(request):
    tea_list = TeacherInfo.objects.all()
    return render(request, "teainfo.html", {"tea_list":tea_list})

def teaadd(request):
    """  添加教师信息  """
    if request.method == "GET":
        return render(request, "tea_add.html")
    # 获取用户提交的数据
    name = request.POST.get("teachername")
    tid = request.POST.get("teacherid")
    school = request.POST.get("teacherschool")
    pwd = request.POST.get("teacherpwd")

    # 添加到数据库
    TeacherInfo.objects.create(teaname=name, teaid=tid, teaschool=school, password=pwd)
    # 添加成功自动跳转
    return redirect("http://127.0.0.1:8000/teainfo/")

def teadelete(request):
    """删除教师"""
    tea_id = request.GET.get('teaid')
    TeacherInfo.objects.filter(id=tea_id).delete()
    return redirect("http://127.0.0.1:8000/teainfo/")

def teaedit(request, teaid):
    """编辑教师信息"""
    if request.method == "GET":
        tea_obj = TeacherInfo.objects.filter(id=teaid).first()
        return render(request, "tea_edit.html", {"tea_obj": tea_obj})

    # 获取管理员修改后的数据
    name = request.POST.get("teachername")
    tid = request.POST.get("teacherid")
    school = request.POST.get("teacherschool")
    pwd = request.POST.get("teacherpwd")

    TeacherInfo.objects.filter(id=teaid).update(teaname=name, teaid=tid, teaschool=school, password=pwd)
    # 修改成功自动跳转
    return redirect("http://127.0.0.1:8000/teainfo/")

def teasearch(request):
    searchname = request.GET.get("searchname")
    #print(searchname)
    # 这里不加first，当查找不到对象的时候，页面为空
    teacher_obj_search = TeacherInfo.objects.filter(teaname=searchname)#.first()
    # print(teacher_obj_search)
    # print(teacher_obj_search.first())
    return render(request, "tea_search.html", {"searchobj":teacher_obj_search})


######################################################### 登录 注册
def login(request):
    if(request.method == "GET"):
        return render(request, "login.html")

    if(request.method == "POST"):
        option = request.POST.get("option")
        uid = request.POST.get("userid")
        password = request.POST.get("userpwd")
        # print(option, uid, password)
        # print(type(option)) #str
        # 管理员 只有一个账号
        if option == "1":
            if uid == "001" and password == "admin001":
                return redirect("http://127.0.0.1:8000/adminpage/")
            return render(request, "login.html", {"error_msg_pwd": "用户名或密码错误"})
        elif option == "2": # 教师
            teacher = TeacherInfo.objects.filter(teaid=uid).first()
            if teacher is None:
                return render(request, "login.html", {"error_msg_id": "用户不存在，请先注册"})
            if password == teacher.password:
                return HttpResponseRedirect(f"http://127.0.0.1:8000/teapage/?teaid={uid}")
            else:
                return render(request, "login.html", {"error_msg_pwd": "密码错误"})
        else:# 学生
            stu = StuInfo.objects.filter(stuid=uid).first()
            if stu is None:
                return render(request, "login.html", {"error_msg_id": "用户不存在，请先注册"})
            if password == stu.password:
                return HttpResponseRedirect(f"http://127.0.0.1:8000/stupage/?stuid={uid}")
                #return redirect("http://127.0.0.1:8000/student/")
            else:
                return render(request, "login.html", {"error_msg_pwd": "密码错误"})

        # if username == "wjm" and password == "123":
        #     #return HttpResponse("登录成功")
        #     return redirect("https://www.baidu.com")
        #return render(request, "login.html")
        #return render(request, "login.html", {"error_msg":"用户名或密码错误"})

"""
TODO:增加验证，保证输入的学号不能与数据库中有重复
"""
def stusignup(request):
    if request.method == "GET":
        return render(request, "stu_signup.html")
    # 获取用户提交的数据
    studentname = request.POST.get("studentname")
    studentid = request.POST.get("studentid")
    school = request.POST.get("school")
    pwd = request.POST.get("pwd")
    print(studentname,studentid,school,pwd)

    # 添加到数据库
    StuInfo.objects.create(stuname=studentname, stuid=studentid, stuschool=school, password=pwd)
    # 添加成功自动跳转
    return render(request, "stu_signup.html", {"ok_msg":"        注册成功，请点击下方连接返回登录页面！"})

def stupage(request):
    #return render(request, "stu_page.html")
    uid = request.GET.get('stuid')
    return render(request, 'stu_page.html', {'uid': uid})

def showstuinfo(request):
    if request.method == "GET":
        stuid = request.GET.get('stuid')
        obj = StuInfo.objects.filter(stuid=stuid).first()
        return render(request, "show_stu_info.html", {"stuid": stuid, "obj": obj})
    # print("ok")
    # name = request.POST.get("stuname")
    # # stuid = request.POST.get("stuid")# 学号不能改
    # stuschool = request.POST.get("stuschool")
    # stupwd = request.POST.get("stupwd")
    # StuInfo.objects.filter(stuid=stuid).update(stuname=name, stuschool=stuschool, password=stupwd)
    # print("修改完成")

def pay(request):
    if request.method == "GET":
        stuid = request.GET.get("stuid")
        #print(stuid)
        return render(request, "pay.html", {"stuid":stuid})

def teapage(request):
    #return render(request, "stu_page.html")
    uid = request.GET.get('teaid')
    return render(request, 'tea_page.html', {'uid': uid})

def showteainfo(request):
    if request.method == "GET":
        teaid = request.GET.get('teaid')
        obj = TeacherInfo.objects.filter(teaid=teaid).first()
        return render(request, "show_tea_info.html", {"teaid": teaid, "obj": obj})

def adminpage(request):
    return render(request, "admin_page.html")

def uploadpaper(request):
    if request.method == "GET":
        return render(request, "upload_paper.html")
    myexam = Exam.objects.create(title='Exam1')
    question = QuestionOption.objects.create(exam=myexam, content='Question 1 content', options=['A', 'B', 'C'], answer='A')
    # 创建其他题目的实例，以此类推
    options = question.get_options()
    return render(request, "upload_paper.html", {'question': question, 'options': options})

def checkpaper(request):
    return render(request, "check_paper.html")