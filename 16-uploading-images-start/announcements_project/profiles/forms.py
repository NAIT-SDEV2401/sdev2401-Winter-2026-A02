# we're going to build on our modelform
# and the idea that we'll upload the user
# in the view based on request.user.
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

        # profile picture creates a forms.ImageField here
        # docs: https://docs.djangoproject.com/en/5.2/ref/forms/fields/#imagefield