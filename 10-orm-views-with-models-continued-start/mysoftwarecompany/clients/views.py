from django.shortcuts import render, get_object_or_404
from django.db.models import Q
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
    company = get_object_or_404(
        Company,
        id=company_id,
    )
    # use a query parameter
    # for example we have http://localhost:8000/clients/company/10/employees/results/?q=Sop
    # the request.GET will be {"q": "Sop"}
    query = request.GET.get('q') # part of the request url.

    # we're going to use a field lookup to filter in the database.
    employees= None
    if query:
        # I want to filter the companies based on this .
        # take a look at field lookups to perform more of these
        # filters https://docs.djangoproject.com/en/5.2/ref/models/querysets/#field-lookups
        # field looks ups just allow you to customize the way you're filtering items.
        # we're using Q objects here (link to docs: https://docs.djangoproject.com/en/5.2/topics/db/queries/#complex-lookups-with-q-objects)

        employees = company.employees.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
        # this doing
        # SELECT * FROM employees WHERE first_name LIKE '%query%' OR last_name LIKE '%query%'


    return render(
        request,
        'clients/employees_search_results.html',
        {'employees': employees }
    )