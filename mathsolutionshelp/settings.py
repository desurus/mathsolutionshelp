import os
from django.utils.translation import ugettext as _


"""
Django settings for mathsolutionshelp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Admins
ADMINS = (
    ('Sasha', 'okryshchenko@gmail.com'),
)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')+swlo*55-#yoyz114v_zmo_bt&pd2evqnad89r8v6z=dcgz5%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'mainsite',
    # 'captcha',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mathsolutionshelp.urls'

WSGI_APPLICATION = 'mathsolutionshelp.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'mainsite.context_processors.get_email_address',
    'mainsite.context_processors.get_testimonials',
    'django.core.context_processors.request',
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mathsolutionshelp',
        'USER': 'mathhelp',
        'PASSWORD': 'w@/4fuY(',
        'HOST': '127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'locale')),
)

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'alexander@dezko.info'
EMAIL_HOST_PASSWORD = '1Voblinda'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'alexander@dezko.info'
EMAIL_USE_TLS = True


# Media files
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'media'))
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')),
)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static')),
)

EMAIL_ADDRESS = 'contacts@mathsolutionshelp.com'

CAPTCHA_OUTPUT_FORMAT = '%(image)s <br/> %(hidden_field)s <div class="captcha-input">%(text_field)s</div>'

SITE_ID = 1
