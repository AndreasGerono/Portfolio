from decouple import config
from Portfolio.settings.common import *  # noqa: F403

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECRET_KEY = config('SECRET_KEY')  # noqa: F405

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
    }
}

# The absolute path to the directory where collectstatic will collect static files for deployment.  # noqa: E501
STATIC_ROOT = os.path.join(BASE_DIR, 'portfolio_projects', 'static')  # noqa: E501, F405
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# The URL to use when referring to static files (where they will be served from)  # noqa: E501
STATIC_URL = '/static/'  # noqa: W292`
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'portfolio_projects', 'static'),  # noqa: F405
]
