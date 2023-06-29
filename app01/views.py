from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from app01.models import StuInfo, TeacherInfo, Exam, QuestionOption, EssayQuestion, AnsOptionQ, AnsEssayQ
from django.db import models
# Create your views here.
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
    return redirect("http://127.0.0.1:4537/stuinfo/")

def studelete(request):
    """删除学生"""
    stu_id = request.GET.get('stuid')
    StuInfo.objects.filter(id=stu_id).delete()
    return redirect("http://127.0.0.1:4537/stuinfo/")

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
    return redirect("http://127.0.0.1:4537/stuinfo/")

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
    return redirect("http://127.0.0.1:4537/teainfo/")

def teadelete(request):
    """删除教师"""
    tea_id = request.GET.get('teaid')
    TeacherInfo.objects.filter(id=tea_id).delete()
    return redirect("http://127.0.0.1:4537/teainfo/")

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
    return redirect("http://127.0.0.1:4537/teainfo/")

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
                return redirect("http://127.0.0.1:4537/adminpage/")
            return render(request, "login.html", {"error_msg_pwd": "用户名或密码错误"})
        elif option == "2": # 教师
            teacher = TeacherInfo.objects.filter(teaid=uid).first()
            if teacher is None:
                return render(request, "login.html", {"error_msg_id": "用户不存在，请先注册"})
            if password == teacher.password:
                return HttpResponseRedirect(f"http://127.0.0.1:4537/teapage/?teaid={uid}")
            else:
                return render(request, "login.html", {"error_msg_pwd": "密码错误"})
        else:# 学生
            stu = StuInfo.objects.filter(stuid=uid).first()
            if stu is None:
                return render(request, "login.html", {"error_msg_id": "用户不存在，请先注册"})
            if password == stu.password:
                return HttpResponseRedirect(f"http://127.0.0.1:4537/stupage/?stuid={uid}")
                #return redirect("http://127.0.0.1:8000/student/")
            else:
                return render(request, "login.html", {"error_msg_pwd": "密码错误"})

        # if username == "wjm" and password == "123":
        #     #return HttpResponse("登录成功")
        #     return redirect("https://www.baidu.com")
        #return render(request, "login.html")
        #return render(request, "login.html", {"error_msg":"用户名或密码错误"})


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
    if request.method == "POST":
        # return render(request, "upload_paper.html")
        exam_title = request.POST.get("exam_title")

        question_content = request.POST.get("question_content")
        options = request.POST.getlist('option')  # 获取所有选项的值
        correct_answer = request.POST.get("correct_answer")
        essay_question = request.POST.get("essay_question")
        essay_answer = request.POST.get("essay_answer")
        # 创建或获取试卷
        exam, _ = Exam.objects.get_or_create(examtitle=exam_title)
        # 创建问题选项
        if exam_title is not None and options is not None and correct_answer is not None:
            QuestionOption.objects.create(
            exam=exam,
            content=question_content,
            options=options,
            correct_answer=correct_answer
            )
            return render(request, "upload_paper.html", {"option_msg": "upload ok"})
        # 创建主观题
        if essay_question is not None and essay_answer is not None:
            EssayQuestion.objects.create(exam=exam, question_text=essay_question, answer_text=essay_answer)
            # 处理上传成功的情况，可以跳转到相应页面或显示成功信息
            return render(request, "upload_paper.html", {"essay_msg":"upload ok"})

    return render(request, "upload_paper.html")

# finishTODO:管理员、教师查看试卷，选择题正确选项显示123而不是ABC
def viewpaper(request):
    # exam = Exam.objects.get(id=exam_id)
    exam = Exam.objects.get(examtitle="exam1")
    questions = QuestionOption.objects.filter(exam=exam)
    essay_questions = EssayQuestion.objects.filter(exam=exam)
    context = {
        'exam': exam,
        'questions': questions
    }
    return render(request, 'view_paper.html', {'user':"管理员",'exam': exam, 'questions': questions, 'essay_questions':essay_questions
                                               ,'index_map':{'0': 'A', 1: 'B','2': 'C'}})

def teaviewpaper(request):
    # exam = Exam.objects.get(id=exam_id)
    exam = Exam.objects.get(examtitle="exam1")
    questions = QuestionOption.objects.filter(exam=exam)
    essay_questions = EssayQuestion.objects.filter(exam=exam)
    context = {
        'exam': exam,
        'questions': questions
    }
    return render(request, 'view_paper.html', {'user':"教师用户",'exam': exam, 'questions': questions, 'essay_questions':essay_questions
                                               ,'index_map':{'0': 'A', 1: 'B','2': 'C'}})

def exam(request,stuid):
    # if request.method == "GET":
    # stuid = request.GET.get("stuid")
        #print(stuid)
    student = StuInfo.objects.filter(stuid=stuid).first()
    exam = Exam.objects.get(examtitle="exam1")
    questions = QuestionOption.objects.filter(exam=exam)
    essay_questions = EssayQuestion.objects.filter(exam=exam)
    if request.method == "POST":
        for count, optQ in enumerate(questions):
            optQid = optQ.id
            ############ 需要加一，html循环索引从1开始
            optAns = request.POST.get("opt_answer"+str(count+1))
            # 选择题自动计分
            if optQ.is_correct(optAns):
                score = 5
            else:
                score = 0
            #print(student, optAns, score)
            AnsOptionQ.objects.create(stuid=student, optQid=optQ, stuAns=optAns, score=score)

        for count, essQ in enumerate(essay_questions):
            essQid = essQ.id
            essAnswer = request.POST.get("stu_essay_answer"+str(count+1))
            #print(essQid, essAnswer)
            AnsEssayQ.objects.create(stuid=student, essQid=essQ, stuAns=essAnswer)
            #print(student,essQ,essAnswer)
        return HttpResponseRedirect(f"http://127.0.0.1:4537/stupage/?stuid={stuid}")

    return render(request, "exam.html", {"stuid":stuid,'exam': exam, 'questions': questions, 'essay_questions':essay_questions})

def teatoscore(request,teaid):
    # 学生对象的索引
    stus_ids = AnsEssayQ.objects.values('stuid').distinct()
    stus = []
    for item in stus_ids:
        # 后面要加first才能获取数据对象！！！
        student = StuInfo.objects.filter(id=item['stuid']).first()
        stus.append(student)
    # print(stus)
    return render(request,"tea_to_score.html",{"teaid":teaid, "students":stus})

def teascorepaper(request,teaid,stuid):
    # stuid = "1001"
    student = StuInfo.objects.filter(stuid=stuid).first()
    OptAnswers = AnsOptionQ.objects.filter(stuid=student)
    opt_score_total = OptAnswers.aggregate(total_score=models.Sum('score')).get('total_score', 0)

    EssAnswers = AnsEssayQ.objects.filter(stuid=student)
    if request.method == "POST":
        for count, obj in enumerate(EssAnswers):
            score1 = request.POST.get("Q"+str(count+1)+"score")
            print(obj.stuAns, score1)
            obj.score = score1
            obj.save()
        ess_score_total = EssAnswers.aggregate(total_score=models.Sum('score')).get('total_score', 0)
        student.score = opt_score_total + ess_score_total
        student.save()
        return HttpResponseRedirect(f"http://127.0.0.1:4537/teapage/{teaid}/scorepaper/")

    return render(request, "tea_score_paper.html",{"teaid":teaid, "stuid":stuid,"EssAnswers":EssAnswers})

def stuscore(request,stuid):
    student = StuInfo.objects.filter(stuid=stuid).first()
    # 单选题
    OptAnswers = AnsOptionQ.objects.filter(stuid=student)
    opt_score_total = OptAnswers.aggregate(total_score=models.Sum('score')).get('total_score', 0)
    # 主观题
    EssAnswers = AnsEssayQ.objects.filter(stuid=student)
    ess_score_total = EssAnswers.aggregate(total_score=models.Sum('score')).get('total_score', 0)
    all_score = student.score
    # all_score = opt_score_total + ess_score_total
    # student.score = all_score
    # student.save()
    return render(request,"stu_score.html",{"stuid":stuid, "opt_score_total":opt_score_total, "ess_score_total":ess_score_total,
                                            "Opts":OptAnswers,"Esss":EssAnswers, "all_score":all_score})