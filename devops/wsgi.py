import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops.settings")


def application(environ, start_response):

    for key, value in environ.items():
        if isinstance(value, str):
            os.environ[key] = value

    return get_wsgi_application()(environ, start_response)
