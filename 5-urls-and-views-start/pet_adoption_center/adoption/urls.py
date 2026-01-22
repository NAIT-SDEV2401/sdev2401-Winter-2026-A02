# this is the mapping for the adoption app.

# import the path from django
from django.urls import path

# we need to import the views
# from our views.py file.
from .views import home_page
# the reason why it's .views is because
# it's looking at the current folder
# and looking for a views file.
# note home_page is the function

# we need to create the mappings
# connecting the url to a view.
# remove the underscore.
urlpatterns = [
    path(
        "", # this is the url route "" is /
        home_page, # this is view
        name="home_page" # we'll use this
        # the template later when making
        # a link to this page.
    )
]