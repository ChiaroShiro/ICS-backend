from ..views.oj import AnnouncementAPI
from django.urls import re_path

urlpatterns = [
    re_path(r"^announcement/?$", AnnouncementAPI.as_view(), name="announcement_api"),
]
