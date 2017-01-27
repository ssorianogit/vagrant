SECRET_KEY = 'secret_string'
TIME_ZONE = 'Europe/Madrid'
LOG_RENDERING_PERFORMANCE = True
LOG_CACHE_PERFORMANCE = True
LOG_METRIC_ACCESS = True
GRAPHITE_ROOT = '/usr/share/graphite-web'
CONF_DIR = '/etc/graphite'
STORAGE_DIR = '/var/lib/graphite/whisper'
CONTENT_DIR = '/usr/share/graphite-web/static'
WHISPER_DIR = '/var/lib/graphite/whisper'
LOG_DIR = '/var/log/graphite'
INDEX_FILE = '/var/lib/graphite/search_index'  # Search index file
USE_REMOTE_USER_AUTHENTICATION = True
DATABASES = {
    'default': {
        'NAME': 'graphite',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'graphite',
        'PASSWORD': 'graphite',
        'HOST': '127.0.0.1',
        'PORT': ''
    }
}