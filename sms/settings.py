"""
Django settings for sms project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q8m^8#0ittoaur@m2u7kw-d3m=$zxl20ht-bii6m+hg771@-gy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'social.apps.SocialConfig',
    'website.apps.WebsiteConfig',
    'payment.apps.PaymentConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'sms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'local': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sms',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 5432,
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd5sra48dh9gf7a',
        'USER': 'pgykxdqbbamphc',
        'PASSWORD': '5836e3cf37f231785b179633598babd14f4edd5021bb67bacc1ef7fb457951b5',
        'HOST': 'ec2-54-163-246-193.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True






PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
'''STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)'''
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

#STATIC_URL = '/static/'
STATIC_FILES = '/staticfiles/'
#STATIC_ROOT = os.path.join(BASE_DIR, STATIC_FILES)
STATICFILES_DIRS = ['.' + STATIC_URL, ]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'






# for login

LOGIN_REDIRECT_URL = 'user'

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

'''EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'projectsms2018@gmail.com'
EMAIL_HOST_PASSWORD = 'projectsms@2018'
DEFAULT_EMAIL_FROM= 'projectsms2018@gmail.com'
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
'''

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'projectsms'
EMAIL_HOST_PASSWORD = 'projectsms@2018'
DEFAULT_EMAIL_FROM= 'info@sms.com'
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'



ADMIN=(
    (
        "sidharth","sidhu.svs@gmail.com"
    ),
    (
        "nissam","nissam514@gmail.com"
    ),
    (
        "joel","joelvarapuram@gmail.com"
    ),
    (
        "admin","projectsms2018@gmail.com"
    )
)

#mail_admin(subject,body)

STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", "pk_test_qKiQoF8KcHUCLEnhknxUceuN")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "sk_test_WNZTOxLXJB1DfJuSjWFbUIb5")
#pg_dump -d sms -h localhost --username admin --password -fp