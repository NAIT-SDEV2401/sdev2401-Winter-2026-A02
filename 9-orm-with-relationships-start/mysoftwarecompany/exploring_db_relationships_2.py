import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

roles_data = [
    {"name": "CEO", "description": "Chief Executive Officer"},
    {"name": "Manager", "description": "Manages a team of employees"},
    {"name": "Developer", "description": "Writes code and develops software"}
]