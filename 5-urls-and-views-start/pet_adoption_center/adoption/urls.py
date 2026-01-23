# this is the mapping for the adoption app.

# import the path from django
from django.urls import path

# we need to import the views
# from our views.py file.
from .views import home_page

urlpatterns = [
    path(
        "", # this is the url route "" is /
        home_page, # this is view
        name="home_page" # we'll use this
        # the template later when making
        # a link to this page.
    )
]















