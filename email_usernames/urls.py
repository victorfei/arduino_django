"""
Urls for email_usernames, which is a third-party app used for registering
using email and without a need for a username.

This app is depended on third-party app 'django-registration'

Adapted by:
    Victor Fei

Downloaded from:
    https://bitbucket.org/hakanw/django-email-usernames/

"""
from django.conf.urls import *

urlpatterns = patterns('email_usernames.views',
    url(r'^login/$', 'email_login', name="email-login"), 
)

try:
    from registration.views import register
    from email_usernames.forms import EmailRegistrationForm
    urlpatterns += patterns('', 
        url(r'^register/$', register, { 'form_class':EmailRegistrationForm }, name="email-register"),
    )
except ImportError:
    pass