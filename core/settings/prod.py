from .base import *

from dj_database_url import parse as dburl

# DATABASES
default_dburl = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")

DATABASES = {
    "default": config("DATABASE_URL", default=default_dburl, cast=dburl),
}

# SECURE APPLICATION
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_PRELOAD = True
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 2592000
SECURE_FRAME_DENY = True

# STATIC FILES
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

AWS_DEFAULT_ACL = "public-read"

AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

AWS_LOCATION = "static"

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {"Access-Control-Allow-Origin": "*"}

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"

MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
