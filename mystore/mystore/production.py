from .settings import *  # noqa

DEBUG = False
DATABASES["default"] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ.get("DB_NAME"),
    'USER': os.environ.get("DB_USER"),
    'PASSWORD': os.environ.get("DB_PASSWORD"),
    'HOST': os.environ.get("DB_HOST"),
    'PORT': '5432',
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa F405
DATABASES["default"]["CONN_MAX_AGE"] = os.environ.get.int("CONN_MAX_AGE", default=60)  # noqa F405
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = os.environ.get.bool("DJANGO_SECURE_SSL_REDIRECT", default=False)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
SECURE_HSTS_PRELOAD = os.environ.get.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = os.environ.get.bool("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)
INSTALLED_APPS += ["storages"]  # noqa F405
AWS_KEY = os.environ.get("AWS_KEY_ID")
AWS_SECRET = os.environ.get("AWS_SECRET")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_QUERYSTRING_AUTH = False
_AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate"}
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME", default=None)
AWS_S3_CUSTOM_DOMAIN = os.environ.get("DJANGO_AWS_S3_CUSTOM_DOMAIN", default=None)
aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
STATICFILES_STORAGE = "django_aws_lambda.utils.StaticRootS3Boto3Storage"
COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
STATIC_URL = f"https://{aws_s3_domain}/static/"
DEFAULT_FILE_STORAGE = "django_aws_lambda.utils.MediaRootS3Boto3Storage"
MEDIA_URL = f"https://{aws_s3_domain}/media/"
MEDIAFILES_LOCATION = "/media"

STATICFILES_LOCATION = "/static"
TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]