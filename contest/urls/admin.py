#from django.conf.urls import url

from django.urls import path

from ..views.admin import ContestAnnouncementAPI, ContestAPI, ACMContestHelper, DownloadContestSubmissions

urlpatterns = [

    path("contest/", ContestAPI.as_view(), name="contest_admin_api"),
    path("contest/announcement/", ContestAnnouncementAPI.as_view(), name="contest_announcement_admin_api"),
    path("contest/acm_helper/", ACMContestHelper.as_view(), name="acm_contest_helper"),
    path("download_submissions/", DownloadContestSubmissions.as_view(), name="acm_contest_helper")
]

"""
    API 说明：

        本文件定义了 网站管理端中 网站管理员admin/超级管理员super-admin两种权限级别的用户 进行 比赛功能的相关管理

        其具体功能包括 在 创建比赛、发布比赛公告等内容

"""
