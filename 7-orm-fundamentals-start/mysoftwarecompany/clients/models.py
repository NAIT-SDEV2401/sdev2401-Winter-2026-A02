from django.db import models

# classes that inherit from models.Model are going
# to be what's in the database.
class Company(models.Model):
    # below here is going to be fields in the database
    name = models.CharField(max_length=100)

    email = models.EmailField(max_length=100, unique=True)


    def __str__(self):
        return self.name