from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'tests.views.normal_view'),
    url(r'^hacking/$', 'tests.views.hacking_attempt'),
)
