from django.db import models

# Create your models here.
# 对数据库进行操作

class StuInfo(models.Model):
    # 学生信息：用户名 身份证号 密码 得分
    username = models.CharField(max_length=32)
    stuid = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    score = models.IntegerField(null=True, blank=True)
    # 其他用户信息字段

class TeacherInfo(models.Model):
    # 教师信息：工号 密码
    teacherid = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

##### 新增数据，不在这里添加
#TeacherInfo.objects.create(teacherid='t001', password='t001')