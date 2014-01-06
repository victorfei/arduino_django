from django.conf.urls import patterns, include, url
from views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # landing
    url(r'^$', landing),
    # profile
    url(r'', include('users.urls', namespace="users")),
    url(r'^admin/', include(admin.site.urls)),
    
    # url settings for django-registration-1.0, which is a third party app.
    url(r'', include('registration.backends.default.urls')),
)
