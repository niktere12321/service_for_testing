import os

from django.core.wsgi import get_wsgi_application

if os.path.isfile(os.path.join(os.path.dirname(__file__), 'settings_local.py')):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings_local")
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.base_settings')

application = get_wsgi_application()
