from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from GymHouse.forms import NewEntryForm
from mainpage.models import Profile


"""
def index(request):
    return HttpResponse("This is the create new entry page for trainers");
"""


@login_required
def create_new_entry(request):
    context = {'user': request.user, 
            'logged_in': request.user.is_authenticated,
            'form': NewEntryForm()}

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewEntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print("gonna save")
            #####form.save()
            new_event = form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."
            creator_profile=Profile.objects.get(user=request.user)
            new_event.creator = creator_profile # Set the user object here
            new_event.save() # Now you can send it to DB
            print("EVENT SAVED!?")
            return HttpResponse("Thanks for that")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewEntryForm()

    context['form']=form
    return render(request, 'create/new_entry_template.html', context);
