"""
Django settings for djangonautic project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g*m)_fy5!11c!r7wfb-_jf=q+$hyh63#z2q^0odffd8ehlj!h)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'https://mydjapp1.herokuapp.com/']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',
    'account',
     'admin_honeypot',
    'defender',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'defender.middleware.FailedLoginMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'djangonautic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'djangonautic.wsgi.application' 

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators



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
# https://docs.djangoproject.com/en/2.0/topics/i18n/


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/blogbuster/djangonautic/assets'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)
# set to create and upload the media for the blogs that we want to add
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



#! To enable the XSS filter in the browser, and force it to always block suspected XSS attacks
SECURE_BROWSER_XSS_FILTER = True

#! To prevent the browser from guessing the content type and force it to always use the type provided in the Content-Type header.
SECURE_CONTENT_TYPE_NOSNIFF = True


#! SecurityMiddleware will permanently (HTTP 301) redirect all HTTP connections to HTTPS
#SECURE_SSL_REDIRECT = True 
#CSRF_COOKIE_SECURE = True
#CSRF_COOKIE_SAMESITE = 'Strict'
#SESSION_COOKIE_SECURE = True

#! To prevent clickjacking:  
X_FRAME_OPTIONS = 'DENY'


#! These force the site to use HTTPS only for the specified time. No HTTP is entertained over the site and if force attempted, 
#  the site by default remembers to force HTTPS 
#SECURE_HSTS_SECONDS = 300  # set low, but when site is ready for deployment, set to at least 15768000 (6 months)
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_HSTS_PRELOAD = True