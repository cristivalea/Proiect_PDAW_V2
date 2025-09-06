"""
WSGI config for Magazin_Online_V2 project.

Expune obiectul WSGI ca variabilă de modul, numit `application`.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Magazin_Online.settings')

application = get_wsgi_application()
