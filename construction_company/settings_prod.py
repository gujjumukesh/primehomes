from .settings import *
import os

DEBUG = False

ALLOWED_HOSTS = [
    'primehomes-cytcukv7f-mukeshrock809-2432s-projects.vercel.app',
    '.vercel.app', # Allow all subdomains of vercel.app
]

# Use environment variable for SECRET_KEY in production
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

# Add other production specific settings here
# For example, database settings for production, static files handling etc.
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_prod')
