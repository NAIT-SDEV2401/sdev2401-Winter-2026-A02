from django.db import models

# you don't have to know how the migrations run
# all you need to know is that it's creating/altering
# the table.

# classes that inherit from models.Model are going
# to be what's in the database.
class Company(models.Model):
    # below here is going to be fields in the database
    name = models.CharField(max_length=100)
    # this goign to make a column in the table named
    # name with max character length of 100
    email = models.EmailField(max_length=100, unique=True)
    # this goign to make a column in the table named
    # email with max character length of 100
    # except it needs to unique

    def __str__(self):
        return self.name