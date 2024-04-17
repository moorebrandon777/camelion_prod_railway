"""
Django settings for camelion project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# importing cloudinary
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

PORT = int(os.environ.get("PORT", 8000))

ALLOWED_HOSTS = ['camelion-prod.up.railway.app','localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",

    'frontend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'camelion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'camelion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'], engine='django_cockroachdb')}


CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5501",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "https://camelion.onrender.com",
    "https://*.camelion.onrender.com",
    "https://tubular-beijinho-926746.netlify.app",
    "https://*.tubular-beijinho-926746.netlify.app"
]

# CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = [
    'POST',
]


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = BASE_DIR / "staticfiles"

# MEDIA_URL =  '/media/'
# MEDIA_ROOT = "/var/lib/data"
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

#cloudinary api config
cloudinary.config( 
  	cloud_name = os.environ.get('CLOUD_NAME'),
  	api_key = os.environ.get('API_KEY'),
  	api_secret = os.environ.get('API_SECRET')
)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CSRF_TRUSTED_ORIGINS = [
    'http://*.127.0.0.1:5500',
    'http://*.127.0.0.1:5500/frontend/my_bg',
    'http://*.127.0.0.1:5501/frontend/my_bg',
    'http://127.0.0.1:8000', 
    'http://*.127.0.0.1:5500/frontend/detail'
    'https://camelion.onrender.com',
    'https://*.camelion.onrender.com',
    'https://*.camelion.onrender.com/frontend/my_bg',
    'https://*.camelion.onrender.com/frontend/detail',
    "https://tubular-beijinho-926746.netlify.app/frontend/my_bg",
    "https://tubular-beijinho-926746.netlify.app/frontend/detail",
    "https://*.tubular-beijinho-926746.netlify.app/frontend/my_bg",
    "https://*.tubular-beijinho-926746.netlify.app/frontend/detail",
    "https://*.camelion-prod.up.railway.app",
    "https://camelion-prod.up.railway.app",
    "https://camelion-prod.up.railway.app/frontend/my_bg",
    "https://camelion-prod.up.railway.app/frontend/detail"
    ]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.privateemail.com'
EMAIL_PORT = 465
# EMAIL_PORT = 587
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'Blue Revelle Inc <headoffice@bluerevelleinc.com>'
