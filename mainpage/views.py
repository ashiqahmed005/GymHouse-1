from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def main_view_not_logged_in(request):
    context = {'variable_example': "This variable was sent from views!"}
    
    return render(request, 'mainpage/mainpage_template.html', context);
    #IF USING TEMPLATE BLOCKS, RENDER THE _CHILD_, NOT THE PARENT


#This decorator ensures that this view can't be accessed unless 
#the user is logged in
@login_required
def main_view_logged_in(request):
	context = {'user': request.user, 
			'logged_in': request.user.is_authenticated}

	return render(request, 'mainpage/mainpage_template.html', context);



""" MOVED TO SCHEDULE
def test(request):
    context = {'test': "teeeesti"}

    return render(request, 'mainpage/test.html', context);
"""