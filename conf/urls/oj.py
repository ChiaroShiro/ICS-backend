#from django.conf.urls import url

from django.urls import path

from ..views import JudgeServerHeartbeatAPI, LanguagesAPI, WebsiteConfigAPI

urlpatterns = [

    path("website/", WebsiteConfigAPI.as_view(), name="website_info_api"),
    path("judge_server_heartbeat/", JudgeServerHeartbeatAPI.as_view(), name="judge_server_heartbeat_api"),
    path("languages/", LanguagesAPI.as_view(), name="language_list_api")
]

"""
    API 说明：

        本文件定义了 网站用户端中 用户 进行 语言设置，网站配置设置以及测评环境配置的能供

        针对用户部分 主要实现 让用户能够自由选择使用的语言(支持简体中文/繁体中文/英语)
                           
"""
