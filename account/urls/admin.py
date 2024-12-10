from django.urls import re_path


from ..views.admin import UserAdminAPI

urlpatterns = [
    re_path(r"^user/?$", UserAdminAPI.as_view(), name="user_admin_api"),
]

"""
    API 说明：
        
        本文件定义了 网站管理端中 网站超级管理员root 进行 用户管理 界面的接口 
        连接 用户管理模块management(管理员账号特有)
            
        主机名/admin/user 路径下可以查看所有的网站用户并进行管理   
        
        功能包括查看当前有哪些用户、导出用户信息、快速生成用户等功能

"""