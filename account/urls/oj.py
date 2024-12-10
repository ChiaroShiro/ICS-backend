from django.urls import re_path

from ..views.oj import (ApplyResetPasswordAPI, ResetPasswordAPI,
                        UserChangePasswordAPI, UserRegisterAPI, UserChangeEmailAPI,
                        UserLoginAPI, UserLogoutAPI, UsernameOrEmailCheck,
                        AvatarUploadAPI, UserProfileAPI, CheckTFARequiredAPI, SessionManagementAPI,
                        OpenAPIAppkeyAPI, SSOAPI)

from utils.captcha.views import CaptchaAPIView

urlpatterns = [

    re_path(r"^login/?$", UserLoginAPI.as_view(), name="user_login_api"),
    re_path(r"^logout/?$", UserLogoutAPI.as_view(), name="user_logout_api"),
    re_path(r"^register/?$", UserRegisterAPI.as_view(), name="user_register_api"),
    re_path(r"^change_password/?$", UserChangePasswordAPI.as_view(), name="user_change_password_api"),
    re_path(r"^change_email/?$", UserChangeEmailAPI.as_view(), name="user_change_email_api"),
    re_path(r"^apply_reset_password/?$", ApplyResetPasswordAPI.as_view(), name="apply_reset_password_api"),
    re_path(r"^reset_password/?$", ResetPasswordAPI.as_view(), name="reset_password_api"),
    re_path(r"^captcha/?$", CaptchaAPIView.as_view(), name="show_captcha"),
    re_path(r"^check_username_or_email", UsernameOrEmailCheck.as_view(), name="check_username_or_email"),
    re_path(r"^profile/?$", UserProfileAPI.as_view(), name="user_profile_api"),
    re_path(r"^upload_avatar/?$", AvatarUploadAPI.as_view(), name="avatar_upload_api"),
    re_path(r"^tfa_required/?$", CheckTFARequiredAPI.as_view(), name="tfa_required_check"),
    re_path(r"^sessions/?$", SessionManagementAPI.as_view(), name="session_management_api"),
    re_path(r"^open_api_appkey/?$", OpenAPIAppkeyAPI.as_view(), name="open_api_appkey_api"),
    re_path(r"^sso?$", SSOAPI.as_view(), name="sso_api")

]

"""
    API 说明：
        
        本文件定义了 网站使用端中 用户 的相关功能模块 
            
        具体功能包括 用户登入登出 用户注册 用户信息修改 等内容

"""
