from django.core.handlers.wsgi import WSGIHandler
import pinax.env
import sys
import os


# setup the environment for Django and Pinax
pinax.env.setup_environ(__file__)


# set application for WSGI processing
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
application = WSGIHandler()
