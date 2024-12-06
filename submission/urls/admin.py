from django.conf.urls import url

from ..views.admin import SubmissionRejudgeAPI

urlpatterns = [
    path("submission/rejudge/", SubmissionRejudgeAPI.as_view(), name="submission_rejudge_api"),
]
