from django.urls import path

# we're going use the view we've created.
from .views import list_companies

urlpatterns = [
    path("", list_companies, name="company_list"),
]