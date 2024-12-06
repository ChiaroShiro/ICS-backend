from django.db import models
from utils.models import JSONField

from account.models import User
from contest.models import Contest
from utils.models import RichTextField
from utils.constants import Choices

# 题目标签模型
class ProblemTag(models.Model):
    name = models.TextField()  # 标签名称

    class Meta:
        db_table = "problem_tag"  # 数据库表名

# 题目规则类型
class ProblemRuleType(Choices):
    ACM = "ACM"  # ACM 模式
    OI = "OI"    # OI 模式

# 题目难度
class ProblemDifficulty(object):
    High = "High"  # 高难度
    Mid = "Mid"    # 中等难度
    Low = "Low"    # 低难度

# 题目输入输出模式
class ProblemIOMode(Choices):
    standard = "Standard IO"  # 标准输入输出
    file = "File IO"          # 文件输入输出

# 默认输入输出模式
def _default_io_mode():
    return {"io_mode": ProblemIOMode.standard, "input": "input.txt", "output": "output.txt"}

# 题目模型
class Problem(models.Model):
    _id = models.TextField(db_index=True)  # 显示ID
    contest = models.ForeignKey(Contest, null=True, on_delete=models.CASCADE)  # 所属比赛
    is_public = models.BooleanField(default=False)  # 是否公开
    title = models.TextField()  # 题目标题
    description = RichTextField()  # 题目描述
    input_description = RichTextField()  # 输入描述
    output_description = RichTextField()  # 输出描述
    samples = JSONField()  # 示例
    test_case_id = models.TextField()  # 测试用例ID
    test_case_score = JSONField()  # 测试用例分数
    hint = RichTextField(null=True)  # 提示
    languages = JSONField()  # 支持的语言
    template = JSONField()  # 代码模板
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    last_update_time = models.DateTimeField(null=True)  # 最后更新时间
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # 创建者
    time_limit = models.IntegerField()  # 时间限制（毫秒）
    memory_limit = models.IntegerField()  # 内存限制（MB）
    io_mode = JSONField(default=_default_io_mode)  # 输入输出模式
    spj = models.BooleanField(default=False)  # 是否为特殊判题
    spj_language = models.TextField(null=True)  # 特殊判题语言
    spj_code = models.TextField(null=True)  # 特殊判题代码
    spj_version = models.TextField(null=True)  # 特殊判题版本
    spj_compile_ok = models.BooleanField(default=False)  # 特殊判题编译是否成功
    rule_type = models.TextField()  # 规则类型
    visible = models.BooleanField(default=True)  # 是否可见
    difficulty = models.TextField()  # 难度
    tags = models.ManyToManyField(ProblemTag)  # 标签
    source = models.TextField(null=True)  # 来源
    total_score = models.IntegerField(default=0)  # 总分（OI模式）
    submission_number = models.BigIntegerField(default=0)  # 提交次数
    accepted_number = models.BigIntegerField(default=0)  # 通过次数
    statistic_info = JSONField(default=dict)  # 统计信息
    share_submission = models.BooleanField(default=False)  # 是否共享提交

    class Meta:
        db_table = "problem"  # 数据库表名
        unique_together = (("_id", "contest"),)  # 唯一约束
        ordering = ("create_time",)  # 排序

    # 增加提交次数
    def add_submission_number(self):
        self.submission_number = models.F("submission_number") + 1
        self.save(update_fields=["submission_number"])

    # 增加通过次数
    def add_ac_number(self):
        self.accepted_number = models.F("accepted_number") + 1
        self.save(update_fields=["accepted_number"])
