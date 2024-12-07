#from django.conf.urls import urls

from django.urls import re_path

from ..views.oj import SubmissionAPI, SubmissionListAPI, ContestSubmissionListAPI, SubmissionExistsAPI

urlpatterns = [
    re_path(r"^submission/?$", SubmissionAPI.as_view(), name="submission_api"),
    re_path(r"^submissions/?$", SubmissionListAPI.as_view(), name="submission_list_api"),
    re_path(r"^submission_exists/?$", SubmissionExistsAPI.as_view(), name="submission_exists"),
    re_path(r"^contest_submissions/?$", ContestSubmissionListAPI.as_view(), name="contest_submission_list_api"),
]

"""
    API 说明：

        本文件定义了 网站用户端中 所有用户 进行一般代码提交/比赛代码提交的功能

"""