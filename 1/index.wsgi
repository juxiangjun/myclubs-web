import sys, os, sae
from myclubs import wsgi
application = sae.create_wsgi_app(wsgi.application)
