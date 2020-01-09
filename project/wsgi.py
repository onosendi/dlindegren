import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'ProductionConfig')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
