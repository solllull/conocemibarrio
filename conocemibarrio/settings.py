"""
Django settings for conocemibarrio project.
Generated by 'django-admin startproject' using Django 4.0.2.
For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+gj0caznve=v!w387ens4gnv2qbz5fjbgl%k6efcvb(j+k0$7z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1']
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'registration',
    'neighborhood',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.gis',
    'cloudinary',
    'forum',
    'ckeditor',
    'pwa',
    'profile',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    #'django.middleware.security.SecurityMiddleware',
]

#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SECURE_SSL_REDIRECT = True
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

ROOT_URLCONF = 'conocemibarrio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'conocemibarrio.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if not os.environ.get("IN_HEROKU"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.mysql',
            'NAME': 'conocemibarrio',
            'USER': 'root',
            'PASSWORD': 'admin1234',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'd3ckt4s3lqv1eq',
            'USER': 'pxxpubfxnxwmvx',
            'PASSWORD': '51bc6ab3e826ca4b097e7b2e5ad93d1c0bae9b70373c8194bbff0678f3d683f9',
            'HOST': 'ec2-52-4-104-184.compute-1.amazonaws.com',
            'PORT': 5432,
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "conocemibarriorafaela@gmail.com"
EMAIL_HOST_PASSWORD = "awlikjxvqibgebtn"

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '497938302411-oud6o1edpt427u169m4i8vs6eu4563it.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.8'
SOCIAL_AUTH_FACEBOOK_KEY = '330003199184031'
SOCIAL_AUTH_FACEBOOK_SECRET = 'cd870cd6be93e9005fe4f20c1bb5965d'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, link'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ('name', 'name'),
    ('email', 'email'),
    ('link', 'profile_url'),
]
SOCIAL_AUTH_URL_NAMESPACE = 'registration:social'

LOGIN_URL = 'registration:logIn'
LOGIN_REDIRECT_URL = 'registration:home'
LOGOUT_URL = 'registration:logOut'
LOGOUT_REDIRECT_URL = 'registration:logIn'

GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH')

CLOUDINARY_URL = 'cloudinary://566164783845727:WoFv-L_mVcqvdBICyWnInT-HbUY@dcexbym30'

cloudinary.config(
    cloud_name="dcexbym30",
    api_key="566164783845727",
    api_secret="WoFv-L_mVcqvdBICyWnInT-HbUY"
)

PWA_APP_NAME = 'conocemibarrio'
PWA_APP_SHORT_NAME = 'conocemibarrio'
PWA_APP_DESCRIPTION = 'conocemibarrio app'
PWA_APP_THEME_COLOR = '#036749'
PWA_APP_BACKGROUND_COLOR = '#FFFFFF'
PWA_APP_START_URL = '/'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ICONS = [
    {
        'src': 'static/img/square.png',
        'sizes': '512x512 192x192',
        "purpose": "maskable any"
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': 'static/img/square.png',
        'sizes': '512x512 192x192',
        "purpose": "maskable any"
    }
]

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'serviceworker.js')
