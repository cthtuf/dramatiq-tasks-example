import os

POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST", "localhost")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': POSTGRESQL_HOST,
        'PORT': 5432,
    }
}
