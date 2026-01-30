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

companies = Company.objects.all()

# let's take a look at the records.
print(companies)
breakpoint()

