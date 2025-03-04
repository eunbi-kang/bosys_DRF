from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-!^+_33%a8m_i*(*mj(v07&y*&@)vm*cqsr2qgq7s)8ft$)l@yd'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "rest_framework",
    "user",
    "book",
    "orders",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# Database 설정
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# MYSQL DB Setting
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # ✅ MySQL 엔진 사용
        'NAME': 'eunbikang',        # ✅ 사용할 데이터베이스 이름
        'USER': 'eunbikang',        # ✅ MySQL 사용자 이름
        'PASSWORD': 'ahffk143',         # ✅ MySQL 비밀번호
        'HOST': 'localhost',        # ✅ 로컬이면 'localhost', 원격이면 IP 주소
        'PORT': '3306',             # ✅ MySQL 기본 포트
        'OPTIONS': {
            'charset': 'utf8mb4',   # ✅ UTF-8 인코딩 설정 (이모지 지원)
        },
    }
}

# postgre DB Setting
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',  # ✅ PostgreSQL 엔진 사용
#         'NAME': 'postgre',        # ✅ 사용할 데이터베이스 이름
#         'USER': 'eunbikang',      # ✅ PostgreSQL 사용자 이름
#         'PASSWORD': '1234',       # ✅ PostgreSQL 비밀번호
#         'HOST': 'localhost',      # ✅ 로컬이면 'localhost', 원격이면 IP 주소
#         'PORT': '5432',           # ✅ PostgreSQL 기본 포트
#     }
# }

# Password validation
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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
