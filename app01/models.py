from django.db import models

# Create your models here.
# 对数据库进行操作

class StuInfo(models.Model):
    # 学生信息：用户名 身份证号 密码
    username = models.CharField(max_length=32)
    stuid = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    # 其他用户信息字段

# class Registration(models.Model):
#     user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
#     # 其他报名信息字段