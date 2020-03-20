from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4v^)0-@of*f)g-d6@c+15kc1h(g-_i#zw09rse-ub=te=$jc62'

ALLOWED_HOSTS = [
	"*"
]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'corona',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
