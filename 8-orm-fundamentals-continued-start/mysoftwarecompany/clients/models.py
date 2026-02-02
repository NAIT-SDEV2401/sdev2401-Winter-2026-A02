from django.db import models


# our model for the client
class Company(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    # let's make changes to the model.
    # we're going to add a nullable field so you don't necessarily
    # need it.
    description = models.TextField(
        blank=True,
        null=True,
        default=""
    )
    # one thing we're to add the time that the object has been created
    created_at = models.DateTimeField(auto_now_add=True)
    # and we're going to add the time that it was last updated
    updated_at = models.DateTimeField(auto_now=True)

    # these are in UTC
    # you want to keep times in UTC in your database so that it's easier to
    # convert to the timezones.
    # Change it in your view.

    def __str__(self):
        return self.name


'''
    # date fields
    # the auto_now_add Automatically set the date when the record is created
    date_joined = models.DateField(auto_now_add=True)
    # the
    updated_at = models.DateField(auto_now=True)
'''