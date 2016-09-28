from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the services page");

# Create your views here.
