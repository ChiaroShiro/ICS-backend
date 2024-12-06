#from django.conf.urls import urls

from django.urls import path

from ..views.oj import SubmissionAPI, SubmissionListAPI, ContestSubmissionListAPI, SubmissionExistsAPI

urlpatterns = [

    path("submission/", SubmissionAPI.as_view(), name="submission_api"),
    path("submissions/", SubmissionListAPI.as_view(), name="submission_list_api"),
    path("submission_exists/", SubmissionExistsAPI.as_view(), name="submission_exists"),
    path("contest_submissions/", ContestSubmissionListAPI.as_view(), name="contest_submission_list_api")

]

"""
    API 说明：

        本文件定义了 网站用户端中 所有用户 进行一般代码提交/比赛代码提交的功能

"""