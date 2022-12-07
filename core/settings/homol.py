from .base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("HOMOL_DATABASE_NAME"),
        "USER": config("HOMOL_DATABASE_USERNAME"),
        "PASSWORD": config("HOMOL_DATABASE_PASSWORD"),
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
