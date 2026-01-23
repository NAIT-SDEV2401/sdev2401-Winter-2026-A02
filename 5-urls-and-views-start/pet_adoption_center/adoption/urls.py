# this is the mapping for the adoption app.

# import the path from django
from django.urls import path

# we need to import the views
# from our views.py file.
from .views import (
    home_page,
    pet_type_details
)
# above, import the view.

urlpatterns = [
    path(
        "", # this is the url route "" is /
        home_page, # this is view
        name="home_page" # we'll use this
        # the template later when making
        # a link to this page.
    ),
    path(
        "pet_type/<str:pet_type>/",
        # above the <str:pet_type> is saying
        # in the url you are expecting a string
        # that is going to be a param to the
        # the view.
        pet_type_details,
        name="pet_type_details"
    )

]















