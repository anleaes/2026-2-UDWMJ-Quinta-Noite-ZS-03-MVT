import os
import sys
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = config('SECRET_KEY', default='django-insecure-salaoapp-zs03-2026')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'core.apps.CoreConfig',
    'categorias.apps.CategoriasConfig',
    'procedimentos.apps.ProcedimentosConfig',
    'avaliacoes.apps.AvaliacoesConfig',
    'agendamentos.apps.AgendamentosConfig',
    'atendimentos.apps.AtendimentosConfig',
    'pagamentos.apps.PagamentosConfig',
    'clientes.apps.ClientesConfig',
    'profissionais.apps.ProfissionaisConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.LoginRequiredMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'salaoapp.urls'
LOGIN_URL = 'core:login'
LOGIN_REDIRECT_URL = 'core:home'
LOGOUT_REDIRECT_URL = 'core:login'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'salaoapp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': config('TNS_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'OPTIONS': {
            'config_dir': config('TNS_ADMIN'),
            'wallet_location': config('TNS_ADMIN'),
            'wallet_password': config('WALLET_PASSWORD'),
        },
    }
}

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'