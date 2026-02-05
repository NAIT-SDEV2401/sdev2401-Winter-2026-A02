import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

from clients.models import Employee, Company

# first select acme inc. from company
# we're going to use .get to select a single instance
COMPANY_NAME = "Acme Inc."
company = Company.objects.get(name=COMPANY_NAME)

breakpoint()