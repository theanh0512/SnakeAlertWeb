"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from app.models import *
import json
from django.core import serializers 

def snakesmap(request):
    snakes = Snake.objects.all();
    snakes_json = json.dumps([snake.dump() for snake in snakes]) ;
    return render(request,'app/snakesmap.html',{'snakes_json':snakes_json});


def snakes(request):
    #return HttpResponse('<html><head><title>Hello, Django!</title></head><body><h1>Hello</h1></body></html>');
    snakes = Snake.objects.all();
    return render_to_response('app/snakes.html',{'snakes': snakes});

def snakedetails(request,id):
    snake = Snake.objects.get(pk= id);
    return render_to_response('app/snakedetails.html',{'snake':snake});

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
