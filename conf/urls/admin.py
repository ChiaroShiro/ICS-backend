from django.urls import re_path
from ..views import WebsiteConfigAPI
from ..views import DashboardInfoAPI

urlpatterns = [
    re_path(r"^website/?$", WebsiteConfigAPI.as_view(), name="website_config_api"),
    re_path(r"^dashboard_info", DashboardInfoAPI.as_view(), name="dashboard_info_api"),
]
