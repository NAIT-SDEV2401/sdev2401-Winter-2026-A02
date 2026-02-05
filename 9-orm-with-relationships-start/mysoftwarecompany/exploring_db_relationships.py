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
    company=acme_company
)

