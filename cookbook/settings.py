"""
Django settings for cookbook project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hv+j&&baaz*n423w-m^#4rn))o*%4s+fwg*+io9q()fx&_!gp1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'recipe',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cookbook.urls'

WSGI_APPLICATION = 'cookbook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
isCodeship = os.getenv('PG_USER', None)
isHeroku = os.getenv('DATABASE_URL', None)

if isHeroku:
	DEFAULT_FILE_STORAGE = 'recipe.s3utils.MediaRootS3BotoStorage'

	AWS_STORAGE_BUCKET_NAME = 'phcookbook-assets'
	AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY') 
	AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID') 



DATABASES = {}
if isCodeship is not None:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'test',
            'USER': os.environ.get('PG_USER'),
            'PASSWORD': os.environ.get('PG_PASSWORD'),
            'HOST': '127.0.0.1',
        }
    }
else:
    import dj_database_url
    DATABASES['default'] = dj_database_url.config(default='postgres://a:a@localhost/cookbook')
    if isHeroku is not None:
        DEBUG = True
# Internationalization # https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
