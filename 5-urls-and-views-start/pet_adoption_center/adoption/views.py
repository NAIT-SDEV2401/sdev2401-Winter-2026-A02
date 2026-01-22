from django.shortcuts import render

# this is going to handle requests
# and give responses to those requests
def home_page(request):
    # for many views we're going to
    # have some type of logic here
    # that will do somethign with the
    # request
    name = "Humane Society"
    # return a response.
    return render(
        request, # pass this to the response
        "adoption/home_page.html", # the template
        { "name": name } # the context passed to
        # the template, and in the template we can
        # use that name variable.
    )
