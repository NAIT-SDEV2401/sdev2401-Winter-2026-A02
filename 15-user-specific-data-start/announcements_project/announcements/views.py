from django.shortcuts import render, redirect
# import login_required decorator
from django.contrib.auth.decorators import (login_required, user_passes_test,
                                            permission_required)
# user passes test is another decorator
# the takes in a function and checks to see if the user
# pass a single test.
# permission_required is a decorator that looks at the permission for a given user
# maybe they're in a group
# if they have a specific permission.



# let's import our is_teacher permission function
from core.permissions import is_teacher


from .forms import AnnouncementForm
from .models import Announcement

@login_required
def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(
        request,
        'announcements/announcement_list.html',
        {'announcements': announcements}
    )

# used from before.
# @user_passes_test(is_teacher, login_url='login')
@login_required
@permission_required(['announcements.add_announcment', 'announcements.change_announcment']) # add permission for this.
def create_announcement(request):
    # let's handle the post.
    if request.method == "POST":
        # pass the data into the form
        form = AnnouncementForm(request.POST)
        # check if form is valid.
        if form.is_valid():
            # we are going to add the created by afterwards
            announcement = form.save(commit=False)
            # create instance but not save it to the db.
            announcement.created_by = request.user
            # the request user is where we can find the
            # user on every request.
            form.save()
            return redirect('announcement_list')
    else:
        form = AnnouncementForm()
    return render(
        request,
        'announcements/create_announcement.html',
        {"form": form}
    )