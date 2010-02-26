from django.conf.urls.defaults import *
import aquatest.views as views

urlpatterns = patterns('',
    (r'^testers$', 'aquatest.views.testers'),
    (r'^testers/add$', 'aquatest.views.testers_add'),
    (r'^testers/(?P<pk>\d+)/edit$', 'aquatest.views.testers_edit'),
    (r'^testers/(?P<pk>\d+)/delete$', 'aquatest.views.testers_delete'),
)