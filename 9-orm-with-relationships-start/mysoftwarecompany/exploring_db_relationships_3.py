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
first_acme_employee = Employee.objects.filter(
    company__name="Acme Inc."
).first() # .first just selects the first one.

# set that employee's role to CEO if it's
# not defined
# you need to get those Roles
ceo_role = Role.objects.filter(name="CEO").first()
# is the same as below.
# ceo_role = Role.objects.get(name="CEO")

if not first_acme_employee.role:
    # example of update.
    first_acme_employee.role = ceo_role
    first_acme_employee.save()
    print("saved.")

print(F"the role of {first_acme_employee} is {first_acme_employee.role}")

