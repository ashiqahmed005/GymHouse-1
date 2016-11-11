from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from mainpage.models import Event
from mainpage.models import Class
import json
from django.core import serializers


"""
def index(request):
    return HttpResponse("This is the schedule/calendar page");
"""
@login_required
def calendar_view(request):
    events = Event.objects.all().order_by('date')
    events = serializers.serialize('json', events)
    classes = Class.objects.all().order_by('begin_date')
    classes = serializers.serialize('json', classes)

    context = {'user': request.user, 
            'logged_in': request.user.is_authenticated,
            'events': events,
            'classes': classes}

    return render(request, 'schedule/schedule_template.html', context);

# Create your views here.
