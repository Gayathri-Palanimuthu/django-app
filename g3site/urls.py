from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from polls.views import *
admin.autodiscover()

urlpatterns = patterns('polls.views',
    url(r'^polls/$', index),
    url(r'^polls/(?P<poll_id>\d+)/$', detail),
    url(r'^polls/(?P<poll_id>\d+)/results/$', results),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', vote),
    url(r'^$', home),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^welcome/$', welcome),
)