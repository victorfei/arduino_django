"""
Views which allow users to manage and edit profile information.

Author(s):
    Victor Fei
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import UserProfile

@login_required
def profile(request):
    """
    Profile page once the user logs in

    """
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=user)
        user_profile.save()

    return render(request, 'users/profile.html',{
        'request': request,
        'user': user,
        'user_profile': user_profile,
    })
