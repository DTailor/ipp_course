from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
import settings

urlpatterns = patterns('',
                       url(r'lab1', include('lab1.urls')),
                       url(r'^', include('labs.urls')),
)
