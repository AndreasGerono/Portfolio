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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
    }
}

# The absolute path to the directory where collectstatic will collect static files for deployment.  # noqa: E501
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # noqa: E501, F405
