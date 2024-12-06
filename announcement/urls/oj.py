#from django.conf.urls import url

from django.urls import path

from ..views.oj import AnnouncementAPI

urlpatterns = [

    path("announcement/", AnnouncementAPI.as_view(), name="announcement_api")
]

"""
    API 说明：

        本文件定义了 网站用户端中 首页 查看由管理员发布的公告的相关信息

        其指向的模块的具体功能为 在网站使用端中 网站首页查看管理员发布的公告

"""
