#from django.conf.urls import url

from django.urls import path

from ..views.oj import ProblemTagAPI, ProblemAPI, ContestProblemAPI, PickOneAPI

urlpatterns = [

    path("problem/tags/", ProblemTagAPI.as_view(), name="problem_tag_list_api"),
    path("problem/", ProblemAPI.as_view(), name="problem_api"),
    path("pickone/", PickOneAPI.as_view(), name="pick_one_api"),
    path("contest/problem/", ContestProblemAPI.as_view(), name="contest_problem_api")
]

"""
    API 说明：

        本文件定义了 网站用户端中 用户 能够进行的 题目操作

        链接的下层功能实现包括: 查看题目的标签，查看比赛中的题目等

"""