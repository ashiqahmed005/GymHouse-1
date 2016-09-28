from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the exercise diary page/profile");

# Create your views here.
