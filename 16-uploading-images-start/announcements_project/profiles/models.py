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


    def __str__(self):
        # looks at the username of the user model.
        return F"Profile of {self.user.username}"
