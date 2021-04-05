from Portfolio.settings.common import *  # noqa: F403

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jnw5@2$04gf$32351rms$lf)vpti&-p%sxa8#c3u7bku#+z4f*'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
    }
}

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'