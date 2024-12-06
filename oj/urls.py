from django.conf.urls import include
from django.urls import path

urlpatterns = [
    #include() 是 Django 中的一个函数，用来引用其他的 URL 配置模块。
    #如include("account.urls.oj")表示该url与下属的account.urls.oj中的对应url拼接

    path("api/", include("account.urls.oj")),
    path("api/admin/", include("account.urls.admin")),
    path("api/", include("announcement.urls.oj")),
    path("api/admin/", include("announcement.urls.admin")),
    path("api/", include("conf.urls.oj")),
    path("api/admin/", include("conf.urls.admin")),
    path("api/", include("problem.urls.oj")),
    path("api/admin/", include("problem.urls.admin")),
    path("api/", include("contest.urls.oj")),
    path("api/admin/", include("contest.urls.admin")),
    path("api/", include("submission.urls.oj")),
    path("api/admin/", include("submission.urls.admin")),
    path("api/admin/", include("utils.urls"))
]

"""
    此处为路由总线，负责将前端传来的所有URL分配给不同的模块的下属URL
"""
