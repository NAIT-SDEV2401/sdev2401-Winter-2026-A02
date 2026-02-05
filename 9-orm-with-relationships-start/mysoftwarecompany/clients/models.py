from django.db import models


# our model for the client
class Company(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    # company description
    description = models.TextField(blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return F"Role(name={self.name})"

# create a Role model
class Role(models.Model):
    # field name Charfield unique, max len 50
    name = models.CharField(max_length=50, unique=True)
    # field description TextField blank and null
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# the employee will have a foreign key to company
# employee -> company (single)
# company -> employee (multiple)
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(
        max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True)

    # Foreign key relationship.
    # employee many to one company
    # if the company is deleted the employees will be deleted.
    # related_name is going to be how you get employees
    # from a company instance.
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='employees'
    )
    # I want you to add a foreignkey to role
    # role
        # Role
        # on_delete models.SET_NULL
        # blank=True
        # null-True
        # related_name employees


    def __str__(self):
        return F"{self.first_name} {self.last_name}" \
            F" works at {self.company.name}"
        # I can access the companies' fields in this model itself.
