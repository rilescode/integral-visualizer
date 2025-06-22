"""
WSGI config for trydjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

# Add the src directory to Python path so trydjango module can be found
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)  # Go up one level to src/
project_root = os.path.dirname(src_dir)  # Go up one more level to project root

# Add both src and project root to Python path
sys.path.insert(0, src_dir)
sys.path.insert(0, project_root)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trydjango.settings")

application = get_wsgi_application()