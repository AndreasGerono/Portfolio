from Portfolio.settings.common import *  # noqa: F403

ALLOWED_HOSTS = ['68.65.122.49', 'localhost']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']  # noqa: F405

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
    }
}

# The absolute path to the directory where collectstatic will collect static files for deployment.  # noqa: E501
STATIC_ROOT = BASE_DIR / 'staticfiles'  # os.path.join(BASE_DIR, 'staticfiles')  # noqa: E501, F405

# The URL to use when referring to static files (where they will be served from)  # noqa: E501
STATIC_URL = '/static/'  # noqa: W292