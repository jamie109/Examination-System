from django.db import models

# Create your models here.
# 对数据库进行操作

class StuInfo(models.Model):
    # 学生信息：用户名 学号 学校 密码 得分
    stuname = models.CharField(max_length=64)
    stuid = models.CharField(max_length=32)
    stuschool = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    score = models.IntegerField(null=True, blank=True)


class TeacherInfo(models.Model):
    # 教师信息：姓名 工号 学校 密码
    teaname = models.CharField(max_length=64)
    teaid = models.CharField(max_length=32)
    teaschool = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

####################################### 试卷 #####################################
class Exam(models.Model):
    examtitle = models.CharField(max_length=64)
# 选择题
class QuestionOption(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    content = models.TextField()
    options = models.JSONField()  # 存储选项的JSON字段
    correct_answer = models.CharField(max_length=1)  # 存储正确选项的值

    def get_options(self):
        return self.options.values()

    def is_correct(self, answer):
        return answer == self.correct_answer

# 主观题
class EssayQuestion(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_text = models.TextField()

######### 考生答题和得分
class AnsOptionQ(models.Model):
    stuid = models.ForeignKey(StuInfo, on_delete=models.CASCADE)
    optQid = models.ForeignKey(QuestionOption, on_delete=models.CASCADE)
    stuAns = models.CharField(null=True, max_length=1)  # 考生选择的答案
    score = models.IntegerField(null=True, blank=True) #考生本题得分

class AnsEssayQ(models.Model):
    stuid = models.ForeignKey(StuInfo, on_delete=models.CASCADE)
    essQid = models.ForeignKey(EssayQuestion, on_delete=models.CASCADE)
    stuAns = models.TextField() #考生答案
    score = models.IntegerField(null=True, blank=True)  # 考生本题得分

# class Answer(models.Model):
#     stuid = StuInfo.stuid

##### 新增数据，不在这里添加
#TeacherInfo.objects.create(teacherid='t001', password='t001')