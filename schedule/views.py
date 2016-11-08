from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from mainpage.models import Event
import json
from django.core import serializers


"""
def index(request):
    return HttpResponse("This is the schedule/calendar page");
"""
@login_required
def calendar_view(request):
    events = Event.objects.all()
    events = serializers.serialize('json', events)

    context = {'user': request.user, 
            'logged_in': request.user.is_authenticated,
            'events': events}

    return render(request, 'schedule/schedule_template.html', context);

# Create your views here.
