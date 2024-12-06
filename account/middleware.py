from django.conf import settings
from django.db import connection
from django.utils.timezone import now
from django.utils.deprecation import MiddlewareMixin

from utils.api import JSONResponse
from account.models import User


class APITokenAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 从请求头中获取应用密钥
        appkey = request.META.get("HTTP_APPKEY")
        if appkey:
            try:
                # 根据应用密钥查找用户
                request.user = User.objects.get(open_api_appkey=appkey, open_api=True, is_disabled=False)
                # 设置CSRF处理完成标志
                request.csrf_processing_done = True
                # 设置认证方法为API密钥
                request.auth_method = "api_key"
            except User.DoesNotExist:
                # 如果用户不存在，则不做任何处理
                pass


class SessionRecordMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 获取请求的IP地址
        request.ip = request.META.get(settings.IP_HEADER, request.META.get("REMOTE_ADDR"))
        if request.user.is_authenticated:
            session = request.session
            # 记录用户代理信息
            session["user_agent"] = request.META.get("HTTP_USER_AGENT", "")
            # 记录IP地址
            session["ip"] = request.ip
            # 记录最后活动时间
            session["last_activity"] = now()
            user_sessions = request.user.session_keys
            # 如果当前会话不在用户的会话列表中，则添加并保存
            if session.session_key not in user_sessions:
                user_sessions.append(session.session_key)
                request.user.save()


class AdminRoleRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 获取请求路径
        path = request.path_info
        # 检查路径是否以/admin/或/api/admin/开头
        if path.startswith("/admin/") or path.startswith("/api/admin/"):
            # 如果用户未登录或没有管理员角色，则返回错误响应
            if not (request.user.is_authenticated and request.user.is_admin_role()):
                return JSONResponse.response({"error": "login-required", "data": "Please login in first"})


class LogSqlMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # 打印SQL查询日志
        print("\033[94m", "#" * 30, "\033[0m")
        time_threshold = 0.03
        for query in connection.queries:
            # 如果查询时间超过阈值，则以警告颜色打印
            if float(query["time"]) > time_threshold:
                print("\033[93m", query, "\n", "-" * 30, "\033[0m")
            else:
                # 否则正常打印
                print(query, "\n", "-" * 30)
        return response
