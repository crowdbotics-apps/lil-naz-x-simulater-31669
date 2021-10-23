"""
WSGI config for lil_naz_x_simulater_31669 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lil_naz_x_simulater_31669.settings')

application = get_wsgi_application()
