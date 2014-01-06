"""
General views for arduino_django project

Author(s):
    Victor Fei
"""
from django.http import HttpResponse, HttpRequest
from django.template.loader import get_template
from django.shortcuts import render
from django.template import Context, RequestContext

def landing(request):
    """ Links to the landing page, where the user can also request invite """
#    if request:
#        text = "GET request got"
    text = request.scheme

    print text
    print "hello"

    return render(request, 'landing.html', {
        'request' : request,
        'text': text,
    })
