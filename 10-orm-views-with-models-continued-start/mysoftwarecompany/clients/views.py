from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Company


def list_companies(request):
    # fetching data from the database and passing it to the template
    companies = Company.objects.all()

    return render(request, 'clients/companies_list.html', {'companies': companies})

# I want to create a detail company view.
def company_detail(request, company_id):
    # we're goign to use the company id.

    return render(
        request,
        'clients/company_detail.html',
    )