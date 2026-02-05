import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

from clients.models import Employee, Company

# first select acme inc. from company
# we're going to use .get to select a single instance
COMPANY_NAME = "Acme Inc."
acme_company = Company.objects.get(name=COMPANY_NAME)

# you can get the employees for this company in
# a couple of ways
all_employees = acme_company.employees.all()
# where "employees" the related_name to company
# on the Employee model.

# from the employee model
all_employees = Employee.objects.filter(
    company=acme_company # this is this instance.
)
print("All Employees are")
print(all_employees)

# creating when you have this foreign key relationship.
# we just need the instance of a company and create
# an employee the same way as before.
# new_employee = Employee.objects.create(
#     # fields that aren't foreignkeys
#     first_name="Gary",
#     last_name="Ricks",
#     email="gary@test.com",
#     # you need to add the instance, note not a queryset.
#     company=acme_company
# )

# let's talk about a second way of creating an item
# you can create the instance and then save
other_employee = Employee(
    first_name="Connor",
    last_name="Hes staying",
    email="connor@test.com",
    company=acme_company
)
# this isn't going to commit to the database yet.
