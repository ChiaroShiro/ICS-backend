#from django.conf.urls import url

from django.urls import path

from ..views.admin import (ContestProblemAPI, ProblemAPI, TestCaseAPI, MakeContestProblemPublicAPIView,
                           CompileSPJAPI, AddContestProblemAPI, ExportProblemAPI, ImportProblemAPI,
                           FPSProblemImport)

urlpatterns = [

    path("test_case/", TestCaseAPI.as_view(), name="test_case_api"),
    path("compile_spj/", CompileSPJAPI.as_view(), name="compile_spj"),
    path("problem/", ProblemAPI.as_view(), name="problem_admin_api"),
    path("contest/problem/", ContestProblemAPI.as_view(), name="contest_problem_admin_api"),
    path("contest_problem/make_public/", MakeContestProblemPublicAPIView.as_view(), name="make_public_api"),
    path("contest/add_problem_from_public/", AddContestProblemAPI.as_view(), name="add_contest_problem_from_public_api"),
    path("export_problem/", ExportProblemAPI.as_view(), name="export_problem_api"),
    path("import_problem/", ImportProblemAPI.as_view(), name="import_problem_api"),
    path("import_fps/", FPSProblemImport.as_view(), name="fps_problem_api")
]

"""
    API 说明：

        本文件定义了 网站管理端中 超级管理员super-admin级别的用户 能够进行的 题目操作
        
        链接的下层功能实现包括: 针对新题目的创建、向一个创建的比赛中导入已有题目等

"""
