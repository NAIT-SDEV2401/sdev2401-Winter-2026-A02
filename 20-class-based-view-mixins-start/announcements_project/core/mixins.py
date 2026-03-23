# we're going to be using
# docs here https://docs.djangoproject.com/en/5.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
from django.contrib.auth.mixins import UserPassesTestMixin

# let's import time
from datetime import datetime


# is we're going to create a mixin that gives us the time
class CurrentTimeMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add the current time to the context
        context["time"] = datetime.now()

        return context


# so this is going to be a class where we define the test
class IsTeacherRoleMixin(UserPassesTestMixin):

    # as per the docs we need to define the "test_func"
    # which will check the permission on the user.
    def test_func(self):
        # this is going to be similar to the
        # is_teacher function
        # we're going to get the user on the self.request
        # which is defined in our class.
        return self.request.user.role == "teacher"
