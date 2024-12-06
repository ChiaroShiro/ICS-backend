#from django.conf.urls import url

from django.urls import path

from ..views.oj import ContestAnnouncementListAPI
from ..views.oj import ContestPasswordVerifyAPI, ContestAccessAPI
from ..views.oj import ContestListAPI, ContestAPI
from ..views.oj import ContestRankAPI

urlpatterns = [

    path("contests/", ContestListAPI.as_view(), name="contest_list_api"),
    path("contest/", ContestAPI.as_view(), name="contest_api"),
    path("contest/password/", ContestPasswordVerifyAPI.as_view(), name="contest_password_api"),
    path("contest/announcement/", ContestAnnouncementListAPI.as_view(), name="contest_announcement_api"),
    path("contest/access/", ContestAccessAPI.as_view(), name="contest_access_api"),
    path("contest_rank/", ContestRankAPI.as_view(), name="contest_rank_api")
]
"""
    API 说明：

        本文件定义了 网站用户端中 用户 进行 参加比赛等的相关功能

        其具体功能包括 在 输入比赛密码加入比赛、查看比赛排名、比赛公告等内容

"""