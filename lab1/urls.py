from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'lab1.views.main', name='index'),

)

