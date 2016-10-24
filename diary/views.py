from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

"""
def index(request):
    return HttpResponse("This is the exercise diary page/profile");
"""
@login_required
def diary_view(request):
    context = {'user': request.user, 
			'logged_in': request.user.is_authenticated}

    return render(request, 'diary/diary_template.html', context);

# Create your views here.
