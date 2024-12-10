from django import forms

from utils.api import serializers, UsernameSerializer

from .models import AdminType, ProblemPermission, User, UserProfile


# 用户登录序列化器
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # 用户名字段
    password = serializers.CharField()  # 密码字段
    tfa_code = serializers.CharField(required=False, allow_blank=True)  # 双因素认证代码字段，可选


# 用户名或邮箱检查序列化器
class UsernameOrEmailCheckSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)  # 用户名字段，可选
    email = serializers.EmailField(required=False)  # 邮箱字段，可选


# 用户注册序列化器
class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32)  # 用户名字段，最大长度32
    password = serializers.CharField(min_length=6)  # 密码字段，最小长度6
    email = serializers.EmailField(max_length=64)  # 邮箱字段，最大长度64
    captcha = serializers.CharField()  # 验证码字段


# 用户修改密码序列化器
class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()  # 旧密码字段
    new_password = serializers.CharField(min_length=6)  # 新密码字段，最小长度6
    tfa_code = serializers.CharField(required=False, allow_blank=True)  # 双因素认证代码字段，可选


# 用户修改邮箱序列化器
class UserChangeEmailSerializer(serializers.Serializer):
    password = serializers.CharField()  # 密码字段
    new_email = serializers.EmailField(max_length=64)  # 新邮箱字段，最大长度64
    tfa_code = serializers.CharField(required=False, allow_blank=True)  # 双因素认证代码字段，可选


# 导入用户序列化器
class ImportUserSeralizer(serializers.Serializer):
    users = serializers.ListField(
        child=serializers.ListField(child=serializers.CharField(max_length=64)))  # 用户列表字段，子元素为最大长度64的字符列表


# 用户管理员序列化器
class UserAdminSerializer(serializers.ModelSerializer):
    real_name = serializers.SerializerMethodField()  # 实名字段，通过方法获取

    class Meta:
        model = User  # 关联的模型
        fields = ["id", "username", "email", "admin_type", "problem_permission", "real_name",
                  "create_time", "last_login", "two_factor_auth", "open_api", "is_disabled"]  # 序列化的字段

    def get_real_name(self, obj):
        return obj.userprofile.real_name  # 获取用户资料中的实名


# 用户序列化器
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # 关联的模型
        fields = ["id", "username", "email", "admin_type", "problem_permission",
                  "create_time", "last_login", "two_factor_auth", "open_api", "is_disabled"]  # 序列化的字段


# 用户资料序列化器
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # 嵌套的用户序列化器
    real_name = serializers.SerializerMethodField()  # 实名字段，通过方法获取

    class Meta:
        model = UserProfile  # 关联的模型
        fields = "__all__"  # 序列化所有字段

    def __init__(self, *args, **kwargs):
        self.show_real_name = kwargs.pop("show_real_name", False)  # 是否显示实名
        super(UserProfileSerializer, self).__init__(*args, **kwargs)

    def get_real_name(self, obj):
        return obj.real_name if self.show_real_name else None  # 根据条件返回实名


# 编辑用户序列化器
class EditUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()  # 用户ID字段
    username = serializers.CharField(max_length=32)  # 用户名字段，最大长度32
    real_name = serializers.CharField(max_length=32, allow_blank=True, allow_null=True)  # 实名字段，最大长度32，可选
    password = serializers.CharField(min_length=6, allow_blank=True, required=False, default=None)  # 密码字段，最小长度6，可选
    email = serializers.EmailField(max_length=64)  # 邮箱字段，最大长度64
    admin_type = serializers.ChoiceField(choices=(AdminType.REGULAR_USER, AdminType.ADMIN, AdminType.SUPER_ADMIN))  # 管理员类型字段
    problem_permission = serializers.ChoiceField(choices=(ProblemPermission.NONE, ProblemPermission.OWN,
                                                          ProblemPermission.ALL))  # 问题权限字段
    open_api = serializers.BooleanField()  # 开放API字段
    two_factor_auth = serializers.BooleanField()  # 双因素认证字段
    is_disabled = serializers.BooleanField()  # 禁用状态字段


# 编辑用户资料序列化器
class EditUserProfileSerializer(serializers.Serializer):
    real_name = serializers.CharField(max_length=32, allow_null=True, required=False)  # 实名字段，最大长度32，可选
    avatar = serializers.CharField(max_length=256, allow_blank=True, required=False)  # 头像字段，最大长度256，可选
    blog = serializers.URLField(max_length=256, allow_blank=True, required=False)  # 博客字段，最大长度256，可选
    mood = serializers.CharField(max_length=256, allow_blank=True, required=False)  # 心情字段，最大长度256，可选
    github = serializers.URLField(max_length=256, allow_blank=True, required=False)  # GitHub字段，最大长度256，可选
    school = serializers.CharField(max_length=64, allow_blank=True, required=False)  # 学校字段，最大长度64，可选
    major = serializers.CharField(max_length=64, allow_blank=True, required=False)  # 专业字段，最大长度64，可选
    language = serializers.CharField(max_length=32, allow_blank=True, required=False)  # 语言字段，最大长度32，可选


# 申请重置密码序列化器
class ApplyResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()  # 邮箱字段
    captcha = serializers.CharField()  # 验证码字段


# 重置密码序列化器
class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()  # 令牌字段
    password = serializers.CharField(min_length=6)  # 密码字段，最小长度6
    captcha = serializers.CharField()  # 验证码字段


# SSO序列化器
class SSOSerializer(serializers.Serializer):
    token = serializers.CharField()  # 令牌字段


# 图片上传表单
class ImageUploadForm(forms.Form):
    image = forms.FileField()  # 图片文件字段


# 文件上传表单
class FileUploadForm(forms.Form):
    file = forms.FileField()  # 文件字段