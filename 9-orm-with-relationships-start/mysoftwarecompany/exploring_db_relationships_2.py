import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

# import role
from clients.models import Role

roles_data = [
    {"name": "CEO", "description": "Chief Executive Officer"},
    {"name": "Manager", "description": "Manages a team of employees"},
    {"name": "Developer", "description": "Writes code and develops software"}
]

# I want you to loop through the dictionaries
for role_data in roles_data:
    role, created = Role.objects.get_or_create(
        name=role_data['name'],
        description=role_data['description'],
    )
    # use get_or_create on the role
    # display if it's created successfully
    if created:
        print("Created new role {role}")
    else:
        print("Selected role {role} from db")
