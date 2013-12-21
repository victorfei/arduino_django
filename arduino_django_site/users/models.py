"""
Models for storing user information and profiles.

Author(s):
    Victor Fei
"""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Stores the information of signed up users or users who requested an invite.
    
    This model extends django authentication model User. In database, the table
    that this model has a connection to is 'auth_user'.
    
    """
    user = models.OneToOneField(User)
    device_id = models.IntegerField(default=0)
    # number of treatment the user has left
    num_treatment_remaining = models.IntegerField(default=0)
    # total treatment in history
    total_treatments = models.IntegerField(default=0)
