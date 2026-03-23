# we're going to be using
# docs here https://docs.djangoproject.com/en/5.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
from django.contrib.auth.mixins import UserPassesTestMixin


# so this is going to be a class where we define the test
class IsTeacherRoleMixin(UserPassesTestMixin):

    # as per the docs we need to define the "test_func"
    # which will check the permission on the user.
    def test_func(self):
        # this is going to be similar to the
        # is_teacher function
        # we're going to get the user on the self.request
        # which is defined in our class.
        breakpoint()
        return self.request.user.role == "Teacher"
