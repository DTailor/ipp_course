from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^/$', 'lab1.views.main', name='index'),
                       url(r'^/task1/$', 'lab1.views.task1', name='task1'),
                       url(r'^/task2/$', 'lab1.views.task2', name='task2'),
                       url(r'^/task3/$', 'lab1.views.task3', name='task3'),

)

