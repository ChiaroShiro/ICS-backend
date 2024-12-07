from django.conf.urls import include
from django.urls import re_path

urlpatterns = [
    re_path(r"^api/", include("account.urls.oj")),
    re_path(r"^api/admin/", include("account.urls.admin")),
    re_path(r"^api/", include("announcement.urls.oj")),
    re_path(r"^api/admin/", include("announcement.urls.admin")),
    re_path(r"^api/", include("conf.urls.oj")),
    re_path(r"^api/admin/", include("conf.urls.admin")),
    re_path(r"^api/", include("problem.urls.oj")),
    re_path(r"^api/admin/", include("problem.urls.admin")),
    re_path(r"^api/", include("contest.urls.oj")),
    re_path(r"^api/admin/", include("contest.urls.admin")),
    re_path(r"^api/", include("submission.urls.oj")),
    re_path(r"^api/admin/", include("submission.urls.admin")),
    re_path(r"^api/admin/", include("utils.urls")),
]

"""
    此处为路由总线，负责将前端传来的所有URL分配给不同的模块的下属URL
"""
