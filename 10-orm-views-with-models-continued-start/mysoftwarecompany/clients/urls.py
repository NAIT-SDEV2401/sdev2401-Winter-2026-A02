from django.urls import path
from .views import list_companies, company_detail, employees_search_results

urlpatterns = [
    path('companies/', list_companies, name='companies_list'),
    # let's create a company detail page.
    path('company/<int:company_id>/', company_detail, name="company_detail"),
    # employee search results
    path('company/<int:company_id>/employees/results/', employees_search_results,
        name="employees_search_results")
]
