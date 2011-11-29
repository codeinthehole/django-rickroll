from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'tests.views.index'),
)
