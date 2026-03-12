from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

# import the model
from .models import Profile

# import form
from .forms import ProfileForm

# create the list of the profiles.
# url
# view
# fetch the profiles
# create the template with the url of the image.
# use the html provided.


@login_required
def profile_list(request):
    profiles = Profile.objects.all()

    return render(
        request,
        "profiles/profile_list.html",
        {"profiles": profiles},
    )


# Create your views here.
@login_required
def update_profile(request):
    # we're going to get or create a profile from the db.
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,  # the images that are passed back.
            instance=profile,
        )
        # check if the form is valid
        if form.is_valid():
            # save the form
            form.save()
            return redirect("profile_edit")
            # redirect to "profile_edit"
    else:
        # render the form
        form = ProfileForm(instance=profile)

    return render(request, "profiles/edit_profile.html", {"form": form})
