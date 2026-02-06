import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

# import Role Employee

# select acme employees
# where company name is Acme Inc.
# Get the first employee

# set that employee's role to CEO if it's
# not defined
# you need to get those Roles