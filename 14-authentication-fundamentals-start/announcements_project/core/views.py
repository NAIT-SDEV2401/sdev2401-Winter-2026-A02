from django.shortcuts import render, redirect # send the user to another page.
from .forms import UserRegistrationForm
# Create your views here.
from django.contrib.auth import login
# login will create a session

def register(request):
    if request.method == "POST":
        # pass the data from the request into form
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save() # this is going to create the user
            login(request, user)
            # login will create the session to login

            # if the login was successful we'll redirect to
            # the announcement_list url
            return redirect('announcement_list')

    else: # is a get or other request
        form = UserRegistrationForm()

    return render(
        request,
        "core/register.html",
        {"form": form}
    )