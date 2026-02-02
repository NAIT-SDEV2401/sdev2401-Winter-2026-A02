from django.shortcuts import render

# Create your views here.

# import the model
from .models import Company

def list_companies(request):

    # get all companies from the database.
    companies = Company.objects.all()

    return render(
        request,
        "clients/companies_list.html",
        {
            "companies": companies
        }
    )
