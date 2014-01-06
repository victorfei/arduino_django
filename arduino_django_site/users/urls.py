"""
Urls for coordinating user profile pages

Author(s):
    Victor Fei
"""

from django.conf.urls import *

urlpatterns = patterns('users.views',
    # profile
    url(r'^profile$', 'profile'),
)
