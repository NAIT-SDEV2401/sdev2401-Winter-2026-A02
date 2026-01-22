from django.contrib import admin
from django.urls import path, include

# pet_adoption_center/urls.py
# this is the project level views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("adoption.urls")),
    # this connects the paths in the adoption
    # to the project at the root of the url
]
