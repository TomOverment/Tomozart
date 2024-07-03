from pathlib import Path
import os
import dj_database_url

print(os.environ.get("DATABASE_URL"))

# Load environment variables from env.py if it exists
if os.path.isfile('env.py'):
    import env

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')


SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')

DEBUG = False

ALLOWED_HOSTS = [
    '8000-tomoverment-tomozart-5f28ojf0go4.ws-eu114.gitpod.io',
    '8000-tomoverment-tomozart-5f28ojf0go4.ws-eu115.gitpod.io',
    '8000-tomoverment-tomozart-5f28ojf0go4.ws-eu115.gitpod.io',
    'your-heroku-app.herokuapp.com',
]

CSRF_TRUSTED_ORIGINS = [
    "https://*.gitpod.io",
    "https://*.herokuapp.com"
]

CSRF_TRUSTED_ORIGIN = os.environ.get("CSRF_TRUSTED_ORIGIN")
if CSRF_TRUSTED_ORIGIN:
    CSRF_TRUSTED_ORIGINS.append(CSRF_TRUSTED_ORIGIN)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'BLOG_APP',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PROJ_TOMO.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'PROJ_TOMO.wsgi.application'

# Database configuration
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# Fallback to SQLite in development
if 'DATABASE_URL' not in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,
'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
