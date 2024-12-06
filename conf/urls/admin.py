#from django.conf.urls import url

from django.urls import path

from ..views import SMTPAPI, JudgeServerAPI, WebsiteConfigAPI, TestCasePruneAPI, SMTPTestAPI
from ..views import ReleaseNotesAPI, DashboardInfoAPI

urlpatterns = [


    path("smtp/", SMTPAPI.as_view(), name="smtp_admin_api"),
    path("smtp_test/", SMTPTestAPI.as_view(), name="smtp_test_api"),
    path("website/", WebsiteConfigAPI.as_view(), name="website_config_api"),
    path("judge_server/", JudgeServerAPI.as_view(), name="judge_server_api"),
    path("prune_test_case/", TestCasePruneAPI.as_view(), name="prune_test_case_api"),
    path("versions/", ReleaseNotesAPI.as_view(), name="get_release_notes_api"),
    path("dashboard_info", DashboardInfoAPI.as_view(), name="dashboard_info_api")
]

"""
    API 说明：

        本文件定义了 网站管理端中 super-admin级别用户(超级管理员) 进行 SMTP(邮件传输协议)配置以及网站配置等功能的路由

        其具体功能包括 在 网站管理端中管理 SMTP设置，包括网站的服务器，邮箱，端口号，基础URL，以及针对是否允许注册的相关开关等

"""
