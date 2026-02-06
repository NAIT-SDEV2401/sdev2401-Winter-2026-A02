import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

# import Role Employee
from clients.models import Employee, Role

# select acme employees
# where company name is Acme Inc.
# Get the first employee
acme_employees = Employee.objects.filter(
    company__name="Acme Inc."
)
breakpoint()

# set that employee's role to CEO if it's
# not defined
# you need to get those Roles