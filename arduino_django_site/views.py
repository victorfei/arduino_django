"""
General views for arduino_django project

Author(s):
    Victor Fei
"""
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from django.template import Context, RequestContext

def landing(request):
    """ Links to the landing page, where the user can also request invite """
    return render(request, 'landing.html', { 'request' : request })
