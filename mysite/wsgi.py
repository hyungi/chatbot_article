"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""
import sys
import os

#sys.path.append(os.path.abspath(os.path.dirname(_file_))+"/..")
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
