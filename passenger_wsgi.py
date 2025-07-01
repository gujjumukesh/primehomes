import os
import sys

from construction_company.wsgi import application

sys.path.insert(0, os.path.dirname(__file__))

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = 'construction_company.settings'
