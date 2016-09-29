from django.shortcuts import render
from django.http import HttpResponse


def main_view_not_logged_in(request):
    context = {'variable_example': "This variable was sent from views!"}
    
    return render(request, 'mainpage/menu.html', context);
    #IF USING TEMPLATE BLOCKS, RENDER THE _CHILD_, NOT THE PARENT

# Create your views here.
