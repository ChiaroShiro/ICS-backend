import hashlib
from datetime import datetime

import pytz
from django.utils import timezone

from account.decorators import super_admin_required
from account.models import User
from contest.models import Contest
from judge.dispatcher import process_pending_task
from options.options import SysOptions
from submission.models import Submission
from utils.api import APIView, CSRFExemptAPIView, validate_serializer
from utils.shortcuts import get_env
from utils.xss_filter import XSSHtml
from .models import JudgeServer
from .serializers import (CreateEditWebsiteConfigSerializer,JudgeServerHeartbeatSerializer)


class WebsiteConfigAPI(APIView):
    def get(self, request):
        ret = {key: getattr(SysOptions, key) for key in
               ["website_base_url", "website_name", "website_name_shortcut",
                "website_footer", "allow_register", "submission_list_show_all"]}
        return self.success(ret)

    @super_admin_required
    @validate_serializer(CreateEditWebsiteConfigSerializer)
    def post(self, request):
        for k, v in request.data.items():
            if k == "website_footer":
                with XSSHtml() as parser:
                    v = parser.clean(v)
            setattr(SysOptions, k, v)
        return self.success()



class JudgeServerHeartbeatAPI(CSRFExemptAPIView):
    @validate_serializer(JudgeServerHeartbeatSerializer)
    def post(self, request):
        data = request.data
        client_token = request.META.get("HTTP_X_JUDGE_SERVER_TOKEN")
        if hashlib.sha256(SysOptions.judge_server_token.encode("utf-8")).hexdigest() != client_token:
            return self.error("Invalid token")

        try:
            server = JudgeServer.objects.get(hostname=data["hostname"])
            server.judger_version = data["judger_version"]
            server.cpu_core = data["cpu_core"]
            server.memory_usage = data["memory"]
            server.cpu_usage = data["cpu"]
            server.service_url = data["service_url"]
            server.ip = request.ip
            server.last_heartbeat = timezone.now()
            server.save(update_fields=["judger_version", "cpu_core", "memory_usage", "service_url", "ip", "last_heartbeat"])
        except JudgeServer.DoesNotExist:
            JudgeServer.objects.create(hostname=data["hostname"],
                                       judger_version=data["judger_version"],
                                       cpu_core=data["cpu_core"],
                                       memory_usage=data["memory"],
                                       cpu_usage=data["cpu"],
                                       ip=request.META["REMOTE_ADDR"],
                                       service_url=data["service_url"],
                                       last_heartbeat=timezone.now(),
                                       )
        # 新server上线 处理队列中的，防止没有新的提交而导致一直waiting
        process_pending_task()

        return self.success()


class LanguagesAPI(APIView):
    def get(self, request):
        return self.success({"languages": SysOptions.languages, "spj_languages": SysOptions.spj_languages})


class DashboardInfoAPI(APIView):
    def get(self, request):
        today = datetime.today()
        today_submission_count = Submission.objects.filter(
            create_time__gte=datetime(today.year, today.month, today.day, 0, 0, tzinfo=pytz.UTC)).count()
        recent_contest_count = Contest.objects.exclude(end_time__lt=timezone.now()).count()
        judge_server_count = len(list(filter(lambda x: x.status == "normal", JudgeServer.objects.all())))
        return self.success({
            "user_count": User.objects.count(),
            "recent_contest_count": recent_contest_count,
            "today_submission_count": today_submission_count,
            "judge_server_count": judge_server_count,
            "env": {
                "FORCE_HTTPS": get_env("FORCE_HTTPS", default=False),
                "STATIC_CDN_HOST": get_env("STATIC_CDN_HOST", default="")
            }
        })
