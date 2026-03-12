from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

# create our bulk assingment upload view

# create the view
@login_required
def bulk_assignment_upload(request)
# that uses the form that we just created
# the get file from the cleaned data
