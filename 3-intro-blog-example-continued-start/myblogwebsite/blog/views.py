from django.shortcuts import render

# we're going import the model
from .models import Post

# Render is a special function in django
# that we'll learn more about that essentially
# returns a template as a response

def post_list(request):
    # lets get the data from the db
    posts = Post.objects.all()


    # one of the things you can do
    # is put a breakpoint to stop
    # the request.
    breakpoint()

    # the line below is going
    # to be what's passed as the response
    return render(
        request,
        'blog/posts_list.html'
    )
    # this is going to look in the templates
    # folder (more on this later.)