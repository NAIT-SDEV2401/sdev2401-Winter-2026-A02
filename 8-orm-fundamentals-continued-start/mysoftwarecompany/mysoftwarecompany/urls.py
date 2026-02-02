from django.contrib import admin
from django.urls import path, include

# we're going to include the clients here

urlpatterns = [
    path("admin/", admin.site.urls),
    path("companies/", include("clients.urls"))
]
