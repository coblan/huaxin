from .base import *
from .logging import*

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'zhaoxiang_gis',
        #'USER': 'postgres',
        #'PASSWORD': '123',
        'USER': 'root',
        'PASSWORD': 'root533',        
        'HOST': '127.0.0.1', 
        'PORT': '5432', 
    },
}


#XUNCHA_HOST = "http://10.235.80.249:8199"
XUNCHA_HOST = 'http://12.110.185.17:8199'
SANGO_BRIDGE='http://12.110.185.17:8499'

ALLOWED_HOSTS=['10.235.80.248']

