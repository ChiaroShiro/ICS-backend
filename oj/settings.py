"""
Django settings for oj project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os
import raven
from copy import deepcopy
from utils.shortcuts import get_env

# 判断是否为生产环境
production_env = get_env("OJ_ENV", "dev") == "production"
if production_env:
    from .production_settings import *
else:
    from .dev_settings import *

# 读取密钥文件
with open(os.path.join(DATA_DIR, "config", "secret.key"), "r") as f:
    SECRET_KEY = f.read()

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Applications
VENDOR_APPS = [
    'django.contrib.auth',  # 认证系统
    'django.contrib.sessions',  # 会话框架
    'django.contrib.contenttypes',  # 内容类型框架
    'django.contrib.messages',  # 消息框架
    'django.contrib.staticfiles',  # 静态文件管理
    'rest_framework',  # Django REST framework
    'django_dramatiq',  # 异步任务队列
    'django_dbconn_retry',  # 数据库连接重试
]

# 如果是生产环境，添加 raven 以支持 Sentry
if production_env:
    VENDOR_APPS.append('raven.contrib.django.raven_compat')

# 本地应用程序 Applications
LOCAL_APPS = [
    'account',  # 用户账户管理
    'announcement',  # 公告管理
    'conf',  # 配置管理
    'problem',  # 问题管理
    'contest',  # 比赛管理
    'utils',  # 工具模块
    'submission',  # 提交管理
    'options',  # 选项管理
    'judge',  # 判题模块
]

# 安装的应用程序
INSTALLED_APPS = VENDOR_APPS + LOCAL_APPS

# 中间件
MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',  # 会话中间件
    'django.middleware.common.CommonMiddleware',  # 通用中间件
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF 防护中间件
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 认证中间件
    'account.middleware.APITokenAuthMiddleware',  # API 令牌认证中间件
    'django.contrib.messages.middleware.MessageMiddleware',  # 消息中间件
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking 防护中间件
    'django.middleware.security.SecurityMiddleware',  # 安全中间件
    'account.middleware.AdminRoleRequiredMiddleware',  # 管理员角色要求中间件
    'account.middleware.SessionRecordMiddleware',  # 会话记录中间件
    # 'account.middleware.LogSqlMiddleware',  # SQL 日志中间件（已注释）
)

# 根 URL 配置
ROOT_URLCONF = 'oj.urls'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # 模板引擎
        'DIRS': [],  # 模板目录
        'APP_DIRS': True,  # 是否在应用程序目录中查找模板
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # 调试上下文处理器
                'django.template.context_processors.request',  # 请求上下文处理器
                'django.contrib.auth.context_processors.auth',  # 认证上下文处理器
                'django.contrib.messages.context_processors.messages',  # 消息上下文处理器
            ],
        },
    },
]

# WSGI 应用程序
WSGI_APPLICATION = 'oj.wsgi.application'

# 密码验证
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # 用户属性相似性验证器
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # 最小长度验证器
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # 常见密码验证器
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # 数字密码验证器
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/public/'  # 静态文件 URL

# 自定义用户模型
AUTH_USER_MODEL = 'account.User'

# 测试用例目录
TEST_CASE_DIR = os.path.join(DATA_DIR, "test_case")
# 日志路径
LOG_PATH = os.path.join(DATA_DIR, "log")

# 头像 URI 前缀
AVATAR_URI_PREFIX = "/public/avatar"
# 头像上传目录
AVATAR_UPLOAD_DIR = f"{DATA_DIR}{AVATAR_URI_PREFIX}"

# 上传前缀
UPLOAD_PREFIX = "/public/upload"
# 上传目录
UPLOAD_DIR = f"{DATA_DIR}{UPLOAD_PREFIX}"

# 静态文件目录
STATICFILES_DIRS = [os.path.join(DATA_DIR, "public")]

# 日志处理程序
LOGGING_HANDLERS = ['console', 'sentry'] if production_env else ['console']
# 日志配置
LOGGING = {
   'version': 1,  # 日志配置版本
   'disable_existing_loggers': False,  # 是否禁用现有的日志记录器
   'formatters': {
       'standard': {
           'format': '[%(asctime)s] - [%(levelname)s] - [%(name)s:%(lineno)d]  - %(message)s',  # 日志格式
           'datefmt': '%Y-%m-%d %H:%M:%S'  # 日期格式
       }
   },
   'handlers': {
       'console': {
           'level': 'DEBUG',  # 日志级别
           'class': 'logging.StreamHandler',  # 日志处理类
           'formatter': 'standard'  # 日志格式化器
       },
       'sentry': {
           'level': 'ERROR',  # 日志级别
           'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',  # Sentry 日志处理类
           'formatter': 'standard'  # 日志格式化器
       }
   },
   'loggers': {
       'django.request': {
           'handlers': LOGGING_HANDLERS,  # 日志处理程序
           'level': 'ERROR',  # 日志级别
           'propagate': True,  # 是否向上传播
       },
       'django.db.backends': {
           'handlers': LOGGING_HANDLERS,  # 日志处理程序
           'level': 'ERROR',  # 日志级别
           'propagate': True,  # 是否向上传播
       },
        'dramatiq': {
            'handlers': LOGGING_HANDLERS,  # 日志处理程序
            'level': 'DEBUG',  # 日志级别
            'propagate': False,  # 是否向上传播
        },
       '': {
           'handlers': LOGGING_HANDLERS,  # 日志处理程序
           'level': 'WARNING',  # 日志级别
           'propagate': True,  # 是否向上传播
       }
   },
}

# REST framework 配置
REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',  # 测试请求默认格式
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',  # 默认渲染器类
    )
}

# Redis URL
REDIS_URL = "redis://%s:%s" % (REDIS_CONF["host"], REDIS_CONF["port"])

# Redis 配置函数
def redis_config(db):
    def make_key(key, key_prefix, version):
        return key

    return {
        "BACKEND": "utils.cache.MyRedisCache",  # 缓存后端
        "LOCATION": f"{REDIS_URL}/{db}",  # 缓存位置
        "TIMEOUT": None,  # 超时时间
        "KEY_PREFIX": "",  # 键前缀
        "KEY_FUNCTION": make_key  # 键函数
    }

# 缓存配置
CACHES = {
    "default": redis_config(db=1)
}

# 会话引擎
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 会话缓存别名  
SESSION_CACHE_ALIAS = "default"

# Dramatiq broker 配置
DRAMATIQ_BROKER = {
    "BROKER": "dramatiq.brokers.redis.RedisBroker",  # Broker 类型
    "OPTIONS": {
        "url": f"{REDIS_URL}/4",  # Redis URL
    },
    "MIDDLEWARE": [
        # "dramatiq.middleware.Prometheus",  # Prometheus 中间件（已注释）
        "dramatiq.middleware.AgeLimit",  # 年龄限制中间件
        "dramatiq.middleware.TimeLimit",  # 时间限制中间件
        "dramatiq.middleware.Callbacks",  # 回调中间件
        "dramatiq.middleware.Retries",  # 重试中间件
        # "django_dramatiq.middleware.AdminMiddleware",  # 管理中间件（已注释）
        "django_dramatiq.middleware.DbConnectionsMiddleware"  # 数据库连接中间件
    ]
}

# Dramatiq 结果后端配置
DRAMATIQ_RESULT_BACKEND = {
    "BACKEND": "dramatiq.results.backends.redis.RedisBackend",  # 结果后端类型
    "BACKEND_OPTIONS": {
        "url": f"{REDIS_URL}/4",  # Redis URL
    },
    "MIDDLEWARE_OPTIONS": {
        "result_ttl": None  # 结果 TTL
    }
}

# Raven 配置
RAVEN_CONFIG = {
    'dsn': 'https://b200023b8aed4d708fb593c5e0a6ad3d:1fddaba168f84fcf97e0d549faaeaff0@sentry.io/263057'  # Sentry DSN
}

# IP 头
IP_HEADER = "HTTP_X_REAL_IP"

# 默认自动字段
DEFAULT_AUTO_FIELD='django.db.models.AutoField'