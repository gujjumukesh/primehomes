import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_company.settings')

# Configure Django
import django
django.setup()

# Create WSGI application
application = get_wsgi_application()

# Vercel serverless function handler
def handler(request, context=None):
    if context is None:
        context = {}
    return application(request, context)

# Alternative handler for different Vercel versions
def handler(request):
    return application(request, None)
