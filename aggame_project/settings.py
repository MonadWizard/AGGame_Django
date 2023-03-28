from pathlib import Path
import os
import config
import datetime


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['*']

CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]

PROJECT_APPS = [
    'auth_user_app',
    'team_app',
    'game_app',
    'tournament_app',
    'home_app',
    'dashboard_app',
]

THIRD_PARTY_APPS = [
    'channels',
    'daphne',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
]

INSTALLED_APPS =  THIRD_PARTY_APPS + CORE_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aggame_project.urls'

AUTH_USER_MODEL = 'auth_user_app.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# WSGI_APPLICATION = 'aggame_project.wsgi.application'
ASGI_APPLICATION = "aggame_project.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USERNAME'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    },
}

# CORS WHITELIST
# CORS_ORIGIN_WHITELIST = [url.strip("'") for url in 
#                         os.environ['CORS_ORIGIN_WHITELIST'].strip('[]').split("', '")]


CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'USER_ID_FIELD': 'userid',
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'aggame_project/static')
    ]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = "/aggame_images/"
MEDIA_ROOT = os.path.join(BASE_DIR, "aggame_images")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST = os.environ['EMAIL_SERVER_HOST']
EMAIL_PORT = os.environ['EMAIL_SERVER_PORT']
EMAIL_HOST_USER = os.environ['EMAIL_SERVER_EMAIL_ADDRESS']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_SERVER_EMAIL_PASSWORD']
EMAIL_USE_TLS = True