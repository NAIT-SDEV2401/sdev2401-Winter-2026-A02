import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

from clients.models import Employee, Role, Company

new_employees_data_acme = [
    {
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice.johnson@acmetesting.com",
        "role": "CEO",
        "company": "Acme Inc.",
    },
    {
        "first_name": "Bob",
        "last_name": "Smith",
        "email": "bob.smith@acmetesting.com",
        "role": "Manager",
        "company": "Acme Inc.",
    },
    {
        "first_name": "Charlie",
        "last_name": "Brown",
        "email": "charlie.brown@acmetesting.com",
        "role": "Developer",
        "company": "Acme Inc.",
    },
]

# for the second part.
new_employees_data_cat_sitting_int = [
    {
        "first_name": "Diana",
        "last_name": "Prince",
        "email": "diana.prince@catsittesting.com",
        "company": "Cat Sitting International",
        "role": "CEO",
    },
    {
        "first_name": "Ethan",
        "last_name": "Hunt",
        "email": "ethan.hunt@catsittesting.com",
        "company": "Cat Sitting International",
        "role": "Manager",
    },
    {
        "first_name": "Fiona",
        "last_name": "Green",
        "email": "fiona.green@catsittesting.com",
        "company": "Cat Sitting International",
        "role": "Developer",
    },
]

# I want you to create a function use the list as a param.
def load_new_employees(list_data):
    # that will loop through the data.
    # create the employees (save them to the db.)
    # add the appropriate relationsships.
    for item in list_data:
        # select role
        role = Role.objects.get(name=item["role"])
        # select company
        company = Company.objects.get(name=item["company"])

        employee, created = Employee.objects.get_or_create(
            first_name=item["first_name"],
            last_name=item["last_name"],
            email=item["email"],
            company=company,
            role=role
        )
        print(F"Employee: {employee}")
        if created:
            print("created.")
        else:
            print("selected from db.")
        print("----------------")

# this shouldn't break if you run it twice.
def main():
    print("loading acme employees")
    load_new_employees(new_employees_data_acme)

if __name__ == "__main__":
    main()