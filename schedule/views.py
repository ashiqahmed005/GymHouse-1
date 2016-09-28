from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the schedule/calendar page");

# Create your views here.
