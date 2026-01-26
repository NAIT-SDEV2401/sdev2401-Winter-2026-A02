from django.contrib import admin

from .models import Company

# we're going to make the company model navigatable
# in the admin.

admin.site.register(Company)
# this is going add our site to the admin
# so that we can add and edit to our hearts
# content.