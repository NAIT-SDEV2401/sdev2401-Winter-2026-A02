from django.db import models
from django.conf import settings


class Profile(models.Model):
    # map a single user to a single profile.
    # it's like a foreignkey but more strict to only map one to one.
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    bio = models.TextField(blank=True, null=True)
    # make a profile picture.
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", # this line will upload to media/profile_pictures/
        blank=True,
        null=True
    )
    # it's a good idea overall to post to different folders.

    def __str__(self):
        # looks at the username of the user model.
        return F"Profile of {self.user.username}"
