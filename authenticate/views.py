from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from mainpage.models import Profile



def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        
        context = {'user': user, 
            'logged_in': request.user.is_authenticated}
        return render(request, 'mainpage/menu.html', context);
    else:
        print("No user found")
        return HttpResponse("NO USER MATCH")


def logout_view(request):
    logout(request)
    print("Logout successfull??")
    return HttpResponse("Logged out successfully")