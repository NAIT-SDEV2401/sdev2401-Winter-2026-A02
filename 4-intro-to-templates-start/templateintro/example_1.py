# we're going take a look at the fundamentals of templates here.

from django.template import Template, Context
# a simple dictionary that has values

data = {
    "rating_topic": "movie",
    "best_rating": 10,
    "worst_rating": 0,
}

