import os
from django.core.asgi import get_asgi_application
from uvicorn.workers import UvicornWorker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'outletavto.settings')

application = get_asgi_application()
