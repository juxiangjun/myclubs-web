from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

def home(request):
    return render_to_response("index.html",{},RequestContext(request))
