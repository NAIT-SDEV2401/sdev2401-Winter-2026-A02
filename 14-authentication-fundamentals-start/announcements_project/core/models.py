from django.db import models

# import the default user that we're going to override.
from django.contrib.auth.models import AbstractUser
# django provides a user by default here but we're going to customize it.

class User(AbstractUser):
    # a tuple is an list that can't be modified
    # treat it as a constant (why it's capitals)
    ROLE_CHOICES = (
        # value on the left, what's display on the right
        ('teacher', 'Teacher'),
        ('student', 'Student')
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES)
    # passing the role choices makes it a drop down
    def __str__(self):
        # Note that username is from the abstract base user.
        return F"{self.username} ({self.role})"
