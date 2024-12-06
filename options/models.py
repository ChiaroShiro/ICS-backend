from django.db import models
from utils.models import JSONField


class SysOptions(models.Model):
    # 定义唯一键字段，并添加数据库索引
    key = models.TextField(unique=True, db_index=True)
    # 定义 JSON 字段
    value = JSONField()
