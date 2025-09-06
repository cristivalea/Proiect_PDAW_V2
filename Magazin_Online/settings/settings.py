"""
Django settings for Magazin_Online_V2 project.

Generat pentru exemplul de magazin online de laptopuri.
"""

import os
from pathlib import Path

# Directorul de bază al proiectului
BASE_DIR = Path(__file__).resolve().parent.parent

# Cheie secretă (nu o folosi în producție)
SECRET_KEY = 'password'

# Pentru dezvoltare, setează DEBUG la True; în producție, la False!
DEBUG = True

ALLOWED_HOSTS = []  # Adaugă domeniile în producție

# Aplicațiile instalate
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',  # Aplicația noastră
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

ROOT_URLCONF = 'Magazin_Online.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'Magazin_Online.wsgi.application'

# Configurarea bazei de date (folosim SQLite pentru dezvoltare)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Folosește motorul MySQL
        'NAME': 'freedb_Magazin_Online',            # Numele bazei de date pe server
        'USER': 'freedb_cristi',         # Utilizatorul de conectare la MySQL
        'PASSWORD': 'e7ZkhXCZtagR$U3',                 # Parola pentru acel utilizator
        'HOST': 'sql.freedb.tech',             # De exemplu: 'localhost' sau IP-ul serverului
        'PORT': '3306',                          # Portul (de obicei 3306)
    }
}

# Configurare parola (minimă) pentru producție; aici e pentru development
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

LANGUAGE_CODE = 'ro'

TIME_ZONE = 'Europe/Bucharest'

USE_I18N = True

USE_TZ = True

# Configurarea fișierelor statice
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'shop/static')]

# Setări pentru fișiere media (dacă se folosesc imagini)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Durata sesiunii (în secunde) - exemplu: 2 săptămâni
SESSION_COOKIE_AGE = 1209600  # 2 weeks

# Sesiunea să nu expire când închizi browserul
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'  # opțional: unde să redirecționeze după autentificare

