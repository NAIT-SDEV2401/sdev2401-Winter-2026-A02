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
