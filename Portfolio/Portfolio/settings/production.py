from decouple import config
from Portfolio.settings.common import *  # noqa: F403

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECRET_KEY = config('SECRET_KEY')  # noqa: F405

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'andrwlkn_portfolio',
        'USER': 'andrwlkn_admin',
        'PASSWORD': 'vd6@qiFP!cu{',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# The absolute path to the directory where collectstatic will collect static files for deployment.  # noqa: E501
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = '/home/andrwlkn/public_html/static'  # noqa: E501, F405
MEDIA_ROOT = '/home/andrwlkn/public_html/media'  # noqa: E501, F405
