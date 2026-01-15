from django.shortcuts import render

# Render is a special function in django
# that we'll learn more about that essentially
# returns a template as a response

def post_list(request):

    # the line below is going
    # to be what's passed as the response
    return render(
        request,
        'blog/posts_list.html'
    )
    # this is going to look in the templates
    # folder (more on this later.)