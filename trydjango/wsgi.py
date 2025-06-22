import os
import sys

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Try multiple possible locations for the trydjango module
possible_paths = [
    current_dir,  # Same directory as wsgi.py
    os.path.dirname(current_dir),  # Parent directory (src/)
    os.path.dirname(os.path.dirname(current_dir)),  # Grandparent (project root)
    '/var/task',  # Vercel task root
    '/var/task/src',  # Vercel src directory
    '/var/task/src/trydjango',  # Direct path to trydjango
]

# Add all existing paths to sys.path
for path in possible_paths:
    if os.path.exists(path) and path not in sys.path:
        sys.path.insert(0, path)

# Also try to find trydjango directory specifically
def find_trydjango_path():
    # Search common locations
    search_roots = ['/var/task', current_dir, os.path.dirname(current_dir)]
    
    for root in search_roots:
        if os.path.exists(root):
            for item in os.listdir(root):
                item_path = os.path.join(root, item)
                if os.path.isdir(item_path):
                    # Check if this directory contains trydjango
                    if 'trydjango' in os.listdir(item_path):
                        trydjango_parent = item_path
                        if trydjango_parent not in sys.path:
                            sys.path.insert(0, trydjango_parent)
                        return trydjango_parent
                    # Or if this IS the trydjango directory
                    elif item == 'trydjango' and os.path.exists(os.path.join(item_path, 'settings.py')):
                        parent = os.path.dirname(item_path)
                        if parent not in sys.path:
                            sys.path.insert(0, parent)
                        return parent
    return None

find_trydjango_path()

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trydjango.settings")

application = get_wsgi_application()