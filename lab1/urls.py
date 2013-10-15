from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^/$', 'lab1.views.main', name='index'),
                       url(r'^/task1/$', 'lab1.views.task1', name='task1'),

)

