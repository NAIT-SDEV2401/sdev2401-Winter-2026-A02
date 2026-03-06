from django.shortcuts import render, redirect
# import login_required decorator
from django.contrib.auth.decorators import login_required

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
            announcement.create_by = request.user
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