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
url_patterns = [

]