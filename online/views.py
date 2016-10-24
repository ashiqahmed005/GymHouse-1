from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



@login_required
def online_view(request):
    context = {'user': request.user, 
			'logged_in': request.user.is_authenticated}

    return render(request, 'online/online_template.html', context);

# Create your views here.
