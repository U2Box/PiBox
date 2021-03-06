from django.conf.urls import patterns, include, url
from django.contrib import admin
from PiApp.views import *
from PiApp.api import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings 

from filebrowser.sites import site
from common import globaldata
import os
import sys

urlpatterns = patterns('',)

cwd  = globaldata.appcwd
list = os.listdir(cwd)
sys.path.append(cwd);

for item in list:
    if os.path.isdir(os.path.join(cwd, item)):
        urlpatterns += patterns ('',
            (r'^' + item + '/', include(item + '.django.urls')),
            )