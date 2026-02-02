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


    def __str__(self):
        return self.name


'''
    # date fields
    # the auto_now_add Automatically set the date when the record is created
    date_joined = models.DateField(auto_now_add=True)
    # the
    updated_at = models.DateField(auto_now=True)
'''