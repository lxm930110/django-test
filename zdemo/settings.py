"""
Django settings for zdemo project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# 工程项目路径
# os.path.abspath(__file__) 获取当前文件的绝对路径
# os.path.dirname(os.path.abspath(__file__))   获取当前文件绝对路劲的上一级路劲 （zdemo）
# os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 获取当前文件绝对路劲的上上一级路劲 zdemo

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('总工程路径:', BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k&@(7vybv+&6j65i3au%k92*p5z4t!-o^j@5edw0eq2#6ke%kl'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式

DEBUG = True

ALLOWED_HOSTS = []

# 生产模式 发布环境使用
# DEBUG = False
# ALLOWED_HOSTS = ['']


# Application definition

# 注册运用
# 添加子运用注册设置

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auser',
    'methods',
    'cresponse',
    'ccookie',
    'csession',
    'add_decorator',
    'dbtest',
]

# 中间件

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #  Django 默认开启了 CSRF 防护，会对上述请求方式进行 CSRF 防护验证，在测试时可以关闭 CSRF 防护机制
    # 'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'middleware.middleware_one', # 注册自定义的中间件
    # 'middleware.middleware_two',    # 注册自定义的中间件
]

ROOT_URLCONF = 'zdemo.urls'

# templates 模板配置

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 部署协议

WSGI_APPLICATION = 'zdemo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# 数据库的配置

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'mysql',
        'NAME': 'django_env',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# 权限认证

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# 本地化

LANGUAGE_CODE = 'zh-Hans'

# 时区

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# 静态文件

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]


# sesssion 缓存在redis进行的配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.107.142:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
