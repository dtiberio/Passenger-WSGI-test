# passenger_wsgi.py
# assumption: the Flask app.py is located on the same folder as this file
# it that's not the case, then update the location: 
# from path.app import MyApp as application
# pull a Flask demo app from here: https://github.com/phusion/passenger-python-flask-demo

from app import MyApp as application
