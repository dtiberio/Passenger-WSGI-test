# passenger_wsgi.py
# testing, place this file in the Parent folder of your Document Root

def application(environ, start_response):
   response_headers = [('Content-type','text/plain')]
   start_response('200 OK', response_headers)
   return ['Hello World!\nThis is a test script.']