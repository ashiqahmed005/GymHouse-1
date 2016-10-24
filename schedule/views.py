from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



"""
def index(request):
    return HttpResponse("This is the schedule/calendar page");
"""
@login_required
def calendar_view(request):
    context = {'user': request.user, 
			'logged_in': request.user.is_authenticated}

    return render(request, 'schedule/schedule_template.html', context);

# Create your views here.
