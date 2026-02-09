from django.urls import path
from .views import list_companies, company_detail

urlpatterns = [
    path('companies/', list_companies, name='companies_list'),
    # let's create a company detail page.
    path('company/<int:company_id>/', company_detail, name="company_detail")
]
