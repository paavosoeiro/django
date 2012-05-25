import os, sys

#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace) 
sys.path.append('C:/Python27/Lib/site-packages/')  



os.environ['DJANGO_SETTINGS_MODULE'] = 'apps.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()