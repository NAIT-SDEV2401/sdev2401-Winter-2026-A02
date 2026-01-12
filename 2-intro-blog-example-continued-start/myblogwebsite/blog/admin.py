from django.contrib import admin

# we're going to import the model
from .models import Post

# register with the admin.
admin.site.register(Post)
