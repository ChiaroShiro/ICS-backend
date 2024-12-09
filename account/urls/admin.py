# from django.conf.urls import url
# 此处使用的是django 1.x 的用法，使用的是正则表达式方法的url

from django.urls import re_path
# django 2.x 以后，一律使用字符串表达的path，可读性高，易于修改


from ..views.admin import UserAdminAPI, GenerateUserAPI

urlpatterns = [

    re_path(r"^user/?$", UserAdminAPI.as_view(), name="user_admin_api"),
    # re_path(r"^generate_user/?$", GenerateUserAPI.as_view(), name="generate_user_api"),
]

"""
    API 说明：
        
        本文件定义了 网站管理端中 网站超级管理员root 进行 用户管理 界面的接口 
        连接 用户管理模块management(管理员账号特有)
            
        主机名/admin/user 路径下可以查看所有的网站用户并进行管理   
        
        功能包括查看当前有哪些用户、导出用户信息、快速生成用户等功能

"""