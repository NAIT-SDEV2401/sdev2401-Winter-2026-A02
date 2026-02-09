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
    company = get_object_or_404(
        Company, # first parameter is the model
        id=company_id, # id is the primary key on the model.
        # company_id is from the request.
        # id always added to the models.
    )

    return render(
        request,
        'clients/company_detail.html',
        {"company": company } # the context passed to the template
    )

# we're going to create a search page.
def employees_search_results(request, company_id):
    # get the company
    # use a query parameter
    # we're going to use a field lookup to filter in the database.


    return render(
        request,
        'clients/employee_search_results.html'
    )