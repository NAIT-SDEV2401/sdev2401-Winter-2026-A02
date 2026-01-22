from django.shortcuts import render

# from the readme
# we're pass this into our template
PET_TYPES = {
    'dog': {
        'name': 'Dog',
        'traits': 'Loyal, energetic, needs space and exercise.',
        'lifestyle_fit': 'active'
    },
    'cat': {
        'name': 'Cat',
        'traits': 'Independent, cuddly, low-maintenance.',
        'lifestyle_fit': 'quiet'
    },
    'rabbit': {
        'name': 'Rabbit',
        'traits': 'Gentle, small, requires calm environment.',
        'lifestyle_fit': 'quiet'
    },
    'parrot': {
        'name': 'Parrot',
        'traits': 'Social, intelligent, needs stimulation.',
        'lifestyle_fit': 'social'
    }
}

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
        {
            "name": name,
            "pet_types": PET_TYPES
        } # the context passed to
        # the template, and in the template we can
        # use that name variable.
    )
