import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

# We're going to import the model so that we
# can interact with it.
from clients.models import Company

# use .objects. to interact with the items.
# let's read all of the items here.

print("Selecting all elements here.")
# select all from the database
companies = Company.objects.all()

# let's take a look at the records.
print(companies)

print("Let's filter to select on a few (subset)")
# select where from the database
acme_company = Company.objects.filter(name="Acme Inc.")
# Acme Inc. is just what I used you can use somethign different.

print("Company filtered for acme inc")
print(acme_company) # this is still queryset which is multiple rows

# select a single instance
cat_company = Company.objects.get(email="cat@test.com")

print("Selecting a single instance")
print(cat_company)


print("Creating items")
# Creating an item in the database.
# equivalent to Insert Into in SQL
# You can only run that once.
# new_company = Company.objects.create(
#     name="Dog Walking co",
#     email="dog@test.com"
# )

# print(new_company)

print("Using get or create")

# second_company below is the instance
# created if the instance we created or not.
second_company, created = Company.objects.get_or_create(
    name="Garys BBQ",
    email="GBBQ@test.com"
)

print("This will be fetched or created")
print(second_company)


# Let's talk about updating the instance
# Update table where in SQL
# we already have the instances
# second_company.name = "Gary and Ricks Steakhouse"
# second_company.email = "GRS@test.com"
# # apply the save
# second_company.save() # this commits to the database.


# delete
second_company.delete()