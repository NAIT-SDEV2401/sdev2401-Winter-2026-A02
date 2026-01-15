# this is going to map the urls in the
# browser to the views itself.
# this is how we connect urls to functionality
from django.urls import path
# import all of the views
from . import views
# the line above is importing all functions
# from views in the current folder

# the paths in our app.
urlspattern = [
    path('', views.post_list, name='post_list')
]

# we're going to add these paths
# to the project using
# urls.py inside of myblogwebsite
# which is the project wide urls.
