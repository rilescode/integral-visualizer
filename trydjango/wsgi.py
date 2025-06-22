"""
WSGI config for trydjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trydjango.settings")

# Initialize Django application
application = get_wsgi_application()

# For Vercel deployment
def handler(request, context):
    """
    Vercel handler function
    """
    return application(request, context)

# Also expose as 'app' for compatibility
app = application