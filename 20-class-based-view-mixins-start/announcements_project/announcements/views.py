from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

# import login_required decorator
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test,
    permission_required,
)

# Let's import the mixin here
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Announcement
from .forms import AnnouncementForm

# docs: https://docs.djangoproject.com/en/5.2/ref/class-based-views/generic-display/#listview
from django.views.generic import ListView

# let's import our custom mixin
# that will check for a teacher
from core.mixins import IsTeacherRoleMixin


# our test function here.
def is_teacher(user):
    # the user object is passed in here by the decorator
    return user.role == "teacher"


# let's rewrite this using our listview generic template
class AnnouncementListView(LoginRequiredMixin, ListView):
    # where in the orm we're fetching
    model = Announcement
    template_name = "announcements/announcement_list.html"
    # this is the variable to loop over in the template
    context_object_name = "announcements"
    ordering = "-created_at"  # most recent first

    # the idea here is that you don't need to write the list view


# instead of using the login_required decorator
# we're going to use the mixin instead of the method decorator.
# docs: https://docs.djangoproject.com/en/5.2/topics/auth/default/#the-loginrequiredmixin-mixin
# class AnnouncementListView(LoginRequiredMixin, View):
#     template_name = "announcements/announcement_list.html"

#     def get(self, request):
#         announcements = Announcement.objects.all().order_by("-created_at")
#         return render(request, self.template_name, {"announcements": announcements})


# we're going to remove the method decorator in favour of our IsTeacherRoleMixin
# this is going to perform the checks for the teacher role and the login required


# class CreateAnnouncementView(IsTeacherRoleMixin, LoginRequiredMixin, View):
#     template_name = "announcements/create_announcement.html"
#     form_class = AnnouncementForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {"form": form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             announcement = form.save(commit=False)
#             announcement.created_by = request.user
#             announcement.save()
#             return redirect("announcement_list")
#         return render(request, self.template_name, {"form": form})
