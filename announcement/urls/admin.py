#from django.conf.urls import url

from django.urls import path

from ..views.admin import AnnouncementAdminAPI

urlpatterns = [

    path("announcement/", AnnouncementAdminAPI.as_view(), name="announcement_admin_api")
]

"""
    API 说明：
        
        本文件定义了 网站管理端中 网站超级管理员super-admin 进行 公告管理 的路由
            
        其指向的模块的具体功能为 在网站管理端中 发布公告并对已有公告进行管理

"""