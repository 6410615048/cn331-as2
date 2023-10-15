
SECRET_KEY = 'hh&*l4q6)&(rec$oj@$v6^e-3*mgwvkkail$t0qt@qi81dy@*f'

DEBUG = False

ALLOWED_HOSTS = ['6410615048.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '6410615048$default',
        'USER': '6410615048',
        'PASSWORD': 'Heroman123',
        'HOST': '6410615048.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'sql_mode': 'traditional',
        },
    }
}

CSRF_TRUSTED_ORIGINS = [
    'http://6410615048.pythonanywhere.com'
]

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, "static")