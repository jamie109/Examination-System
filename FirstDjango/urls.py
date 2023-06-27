"""
URL configuration for FirstDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    # path('user/', views.user),
    #
    # path('user/delete/', views.userdelete),
    # path('tpl/', views.tpl),
    # path('news/', views.news),
    # path('login/', views.login),
    # path('orm/', views.orm),
    #
    ################################ 学生、教师信息管理 增删改查 finish  #############################
    path('stuinfo/', views.stuinfo),
    path('stuinfo/add/', views.stuadd),
    path('stuinfo/delete/', views.studelete),
    path('stuinfo/<int:stuid>/edit/', views.stuedit),
    path('stuinfo/search/', views.stusearch),

    path('teainfo/', views.teainfo),
    path('teainfo/add/', views.teaadd),
    path('teainfo/delete/', views.teadelete),
    path('teainfo/<int:teaid>/edit/', views.teaedit),
    path('teainfo/search/', views.teasearch),

################################ 主页  #############################
    path('login/', views.login),
################################ admin ###########################
    path('adminpage/', views.adminpage),
    path('adminpage/uploadpaper/', views.uploadpaper),
    path('adminpage/viewpaper/', views.viewpaper),
################################ student ###########################
    path('stusignup/', views.stusignup),
    path('stupage/', views.stupage),
    path('stupage/showstuinfo/', views.showstuinfo),
    path('stupage/pay/', views.pay),
    path('stupage/<int:stuid>/exam/', views.exam),
    path('stupage/<int:stuid>/score/', views.stuscore),
################################ teacher ###########################
    path('teapage/', views.teapage),
    path('teapage/showteainfo/', views.showteainfo),
    path('teapage/viewpaper/', views.teaviewpaper),
    path('teapage/<int:teaid>/scorepaper/', views.teatoscore),
    path('teapage/<int:teaid>/scorepaper/<int:stuid>/', views.teascorepaper),
]
