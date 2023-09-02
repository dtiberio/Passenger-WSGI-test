# passenger_wsgi.py

# by default, PassengerAppRoot is the Parent of vhost DocumentRoot, and this file needs to be stored there

import os

# Set the DJANGO_SETTINGS_MODULE environment variable
# Replace 'path.your_project' with your project's actual name, relative to this file
# Update ALLOWED_HOSTS in settings.py
# if needed, touch ./tmp/restart.txt

os.environ['DJANGO_SETTINGS_MODULE'] = 'path.your_project.settings' 

# Import the Django application
from django.core.wsgi import get_wsgi_application

# Create a WSGI application
application = get_wsgi_application()
