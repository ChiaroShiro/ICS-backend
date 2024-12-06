from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.db import models
from utils.models import JSONField

# 管理员类型常量类
class AdminType(object):
    REGULAR_USER = "Regular User"  # 普通用户
    ADMIN = "Admin"  # 管理员
    SUPER_ADMIN = "Super Admin"  # 超级管理员

# 问题权限常量类
class ProblemPermission(object):
    NONE = "None"  # 无权限
    OWN = "Own"  # 拥有者权限
    ALL = "All"  # 全部权限

# 自定义用户管理器
class UserManager(models.Manager):
    use_in_migrations = True

    # 根据自然键获取用户
    def get_by_natural_key(self, username):
        return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": username})

# 用户模型
class User(AbstractBaseUser):
    username = models.TextField(unique=True)  # 用户名
    email = models.TextField(null=True)  # 邮箱
    create_time = models.DateTimeField(auto_now_add=True, null=True)  # 创建时间
    admin_type = models.TextField(default=AdminType.REGULAR_USER)  # 管理员类型
    problem_permission = models.TextField(default=ProblemPermission.NONE)  # 问题权限
    reset_password_token = models.TextField(null=True)  # 重置密码令牌
    reset_password_token_expire_time = models.DateTimeField(null=True)  # 重置密码令牌过期时间
    auth_token = models.TextField(null=True)  # SSO认证令牌
    two_factor_auth = models.BooleanField(default=False)  # 是否启用双因素认证
    tfa_token = models.TextField(null=True)  # 双因素认证令牌
    session_keys = JSONField(default=list)  # 会话密钥
    open_api = models.BooleanField(default=False)  # 是否启用开放API
    open_api_appkey = models.TextField(null=True)  # 开放API应用密钥
    is_disabled = models.BooleanField(default=False)  # 是否禁用

    USERNAME_FIELD = "username"  # 用户名字段
    REQUIRED_FIELDS = []  # 必填字段

    objects = UserManager()  # 用户管理器

    # 判断是否为管理员
    def is_admin(self):
        return self.admin_type == AdminType.ADMIN

    # 判断是否为超级管理员
    def is_super_admin(self):
        return self.admin_type == AdminType.SUPER_ADMIN

    # 判断是否为管理员角色
    def is_admin_role(self):
        return self.admin_type in [AdminType.ADMIN, AdminType.SUPER_ADMIN]

    # 判断是否可以管理所有问题
    def can_mgmt_all_problem(self):
        return self.problem_permission == ProblemPermission.ALL

    # 判断是否为比赛管理员
    def is_contest_admin(self, contest):
        return self.is_authenticated and (contest.created_by == self or self.admin_type == AdminType.SUPER_ADMIN)

    class Meta:
        db_table = "user"  # 数据库表名

# 用户资料模型
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 关联用户
    acm_problems_status = JSONField(default=dict)  # ACM问题状态
    oi_problems_status = JSONField(default=dict)  # OI问题状态

    real_name = models.TextField(null=True)  # 真实姓名
    avatar = models.TextField(default=f"{settings.AVATAR_URI_PREFIX}/default.png")  # 头像
    blog = models.URLField(null=True)  # 博客
    mood = models.TextField(null=True)  # 心情
    github = models.TextField(null=True)  # GitHub
    school = models.TextField(null=True)  # 学校
    major = models.TextField(null=True)  # 专业
    language = models.TextField(null=True)  # 语言
    accepted_number = models.IntegerField(default=0)  # 接受的题目数量（ACM）
    total_score = models.BigIntegerField(default=0)  # 总分（OI）
    submission_number = models.IntegerField(default=0)  # 提交数量

    # 增加接受的题目数量
    def add_accepted_problem_number(self):
        self.accepted_number = models.F("accepted_number") + 1
        self.save()

    # 增加提交数量
    def add_submission_number(self):
        self.submission_number = models.F("submission_number") + 1
        self.save()

    # 增加分数，计算总分时，先减掉上次该题所得分数，然后再加上本次所得分数
    def add_score(self, this_time_score, last_time_score=None):
        last_time_score = last_time_score or 0
        self.total_score = models.F("total_score") - last_time_score + this_time_score
        self.save()

    class Meta:
        db_table = "user_profile"  # 数据库表名
