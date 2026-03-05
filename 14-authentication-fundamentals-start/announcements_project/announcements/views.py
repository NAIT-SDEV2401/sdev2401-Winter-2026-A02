# import the decorator for login_required
# to essentially make sure that user that isn't authenticated
# can't the page.
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

# Create your views here.
from .models import Announcement

# students and teachers can view
# so any one logged in.
def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(
        request,
        'announcements/announcement_list.html',
        {'announcements': announcements}
    )

# we're going to limit this to teachers only.
def create_announcement(request):
    return render(request, 'announcements/create_announcement.html')
