import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_groups_project.settings')

application = get_wsgi_application()
