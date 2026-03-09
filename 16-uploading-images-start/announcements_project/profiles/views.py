from django.contrib.auth.decorators import login_required

from django.shortcuts import render

# import the model
from .models import Profile

# Create your views here.
@login_required
def update_profile(request):
    # we're going to get or create a profile from the db.
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )


