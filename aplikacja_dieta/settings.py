from pathlib import Path
import dj_database_url
import os 
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv('API_KEY')
APP_NAME = os.environ.get("FLY_APP_NAME")
ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev"]

DEBUG = True
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CSRF_TRUSTED_ORIGINS = ['https://zarzadzanie-dieta.fly.dev']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "dieta",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "aplikacja_dieta.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'dieta', 'templates', 'dieta')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "aplikacja_dieta.wsgi.application"


"""
DATABASES = {
    'default': dj_database_url.parse(
        os.getenv('db_connection')
    )
}

DATABASES['default']['OPTIONS'] = {
    'sslmode': 'require',
    'options': 'endpoint=br-wispy-forest-a20d5btq',
}
"""
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.getenv('PGDATABASE'),
    'USER': os.getenv('PGUSER'),
    'PASSWORD': os.getenv('PGPASSWORD'),
    'HOST': os.getenv('PGHOST'),
    'PORT': os.getenv('PGPORT', 12663),
    'OPTIONS': {
      'sslmode': 'require',
    },
    'DISABLE_SERVER_SIDE_CURSORS': True,
  }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
