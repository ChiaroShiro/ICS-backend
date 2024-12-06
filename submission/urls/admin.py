#from django.conf.urls import urls

from django.urls import path

from ..views.admin import SubmissionRejudgeAPI

urlpatterns = [

    path("submission/rejudge", SubmissionRejudgeAPI.as_view(), name="submission_rejudge_api")
]

"""
    API 说明：

        本文件定义了 网站管理端中 网站超级管理员super admin级别用户 的特殊权限——针对已测评程序进行重新评测的功能

"""