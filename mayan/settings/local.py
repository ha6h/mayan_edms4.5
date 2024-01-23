DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mayan',
        'USER': 'mayan',
        'PASSWORD': '2255',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# mayan/settings/local.py
DEFAULT_FILE_STORAGE = 'mayan.apps.storage.settings.storage_backend'
MEDIA_ROOT = '/mayan/media/shared_files'
MEDIA_URL = '/media/'