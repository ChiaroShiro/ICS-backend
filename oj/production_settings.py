from utils.shortcuts import get_env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': get_env("POSTGRES_HOST", "oj-postgres"),  # 使用容器名代替 127.0.0.1
        'PORT': get_env("POSTGRES_PORT", "5432"),  # 默认 PostgreSQL 端口为 5432
        'NAME': get_env("POSTGRES_DB", "onlinejudge"),
        'USER': get_env("POSTGRES_USER", "onlinejudge"),
        'PASSWORD': get_env("POSTGRES_PASSWORD", "onlinejudge")
    }
}


REDIS_CONF = {
    "host": get_env("REDIS_HOST", "oj-redis"),
    "port": get_env("REDIS_PORT", "6379")
}

DEBUG = False

ALLOWED_HOSTS = ['*']

DATA_DIR = "/data"
