# coding=utf-8
import os
from utils.shortcuts import get_env

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # 使用PostgreSQL数据库
        'HOST': get_env('POSTGRES_HOST', '127.0.0.1'),  # 数据库主机
        'PORT': get_env('POSTGRES_PORT', '5435'),  # 数据库端口
        'NAME': get_env('POSTGRES_DB', 'onlinejudge'),  # 数据库名称
        'USER': get_env('POSTGRES_USER', 'onlinejudge'),  # 数据库用户
        'PASSWORD': get_env('POSTGRES_PASSWORD', 'onlinejudge')  # 数据库密码
    }
}

# Redis配置
REDIS_CONF = {
    'host': get_env('REDIS_HOST', '127.0.0.1'),  # Redis主机
    'port': get_env('REDIS_PORT', '6380')  # Redis端口
}

# 调试模式
DEBUG = True

# 允许的主机
ALLOWED_HOSTS = ["*"]

# 数据目录
DATA_DIR = f"{BASE_DIR}/data"
