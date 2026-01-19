import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "templateintro.settings")
django.setup()

print("Django environment set up successfully.")
# everything above this line is needed to create a runnable django file.

from django.template import Template, Context

data = {
    "rating_topic": "Book",
    "best_rating": 5,
    "worst_rating": 1,
    "items": [
        {"title": "brave new world", "rating": 4},
        {"title": "1984",  "rating": 5},
        {"title": "The Great Gatsby", "rating": 4},
        {"title": "Twilight", "rating": 1},
    ]
}

# 1. I want you to create a template that will end up like this
'''
Books rated by us.
- BOOKTITLEHERE rated BOOKRATINGHERE
- BOOKTITLEHERE rated BOOKRATINGHERE
- BOOKTITLEHERE rated BOOKRATINGHERE
- BOOKTITLEHERE rated BOOKRATINGHERE
'''
# I want you to use the {% for ... %} {% endfor %}

# 2. I want you to add the data to a context
# 3. I want you to use template.render and print out the data.