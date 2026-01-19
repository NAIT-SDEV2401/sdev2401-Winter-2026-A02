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
        {"title": "The Great Gatsby", "rating": 3},
        {"title": "Twilight", "rating": 1},
    ]
}

# 1. I want you to create a template that will end up like this
# below is what I want to display
'''
Books rated by us.
- BOOKTITLEHERE rated BOOKRATINGHERE, very good read (IF GREATER OR EQ TO 4)
- BOOKTITLEHERE rated BOOKRATINGHERE, okay read (IF LT 4)
- BOOKTITLEHERE rated BOOKRATINGHERE, skip (IF EQ 1)
- BOOKTITLEHERE rated BOOKRATINGHERE
'''
# I want you to use the {% for ... %} {% endfor %}
# reference in the docs: https://docs.djangoproject.com/en/5.2/ref/templates/language/#tags
template = Template("""
Books rated by us.
{% for book in items %}
- {{ book.title }} rated {{ book.rating }}
  {% if book.rating >= 4 %}very good read{% elif book.rating > 1 %}okay read{% else %}skip{% endif %}
{% endfor %}
""")
# 2. I want you to add the data to a context
context = Context(data)

# 3. I want you to use template.render and print out the data.
print(template.render(context))
