from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'variable_example': "This variable was sent from views!"}
    return render(request, 'mainpage/index.html', context);

    #return HttpResponse("Hello, world. You're at the mainpage.")

# Create your views here.
