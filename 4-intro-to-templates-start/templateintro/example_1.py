import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "templateintro.settings")
django.setup()

print("Django environment set up successfully.")
# Ignore above this line for now

# we're going take a look at the fundamentals of templates here.

from django.template import Template, Context
# a simple dictionary that has values

data = {
    "rating_topic": "movie",
    "best_rating": 10,
    "worst_rating": 0,
}

# we're going to tcreate a template here
# to display information you need to use {{ datahere }} where datahere is a dictionary key
template = Template("""
{{ rating_topic }} will have ratings from {{ best_rating }} to {{ worst_rating }}
where {{ best_rating }} is the best rating.
""")

# put the data into a context
context = Context(data)

# context that we have here.
print(template.render(context))