# override the user creation from from django.
from django import forms
# inherit from UserCreationFrom which is a form based on modelform
# which creates a user.
from django.contrib.auth.forms import UserCreationForm

# since this is based on a modelform we need to import
# our model
from .models import User


class UserRegistrationForm(UserCreationForm):
    # just like a modelform add the meta class
    class Meta:
        # the meta class is just the syntax to create a form
        # based on the model
        model = User
        fields = [
            # add fields from the AbstractUser
            'username',
            'email',
            'password1',
            'password2',
            # we're going to add our custom field
            'role',
        ]
