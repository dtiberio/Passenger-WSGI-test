# passenger_wsgi.py

# by default, PassengerAppRoot is the Parent of vhost DocumentRoot, and this file needs to be stored there
# if you've set the Apache Directive: PassengerAppRoot, then place this file there

import os

# Set the DJANGO_SETTINGS_MODULE environment variable
# Replace 'path.your_project' with your project's actual name, relative to this file
# Update ALLOWED_HOSTS in settings.py
# if needed, touch ./tmp/restart.txt, this is the Passenger restart file

os.environ['DJANGO_SETTINGS_MODULE'] = 'path.your_project.settings' 

# Import the Django application
from django.core.wsgi import get_wsgi_application

# Create a WSGI application
application = get_wsgi_application()
