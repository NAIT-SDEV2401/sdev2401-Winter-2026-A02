import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()

print("Django environment set up successfully.")

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
# that will loop through the data.
# create the employees.
# add the appropriate relationsships.

# this shouldn't break if you run it twice.