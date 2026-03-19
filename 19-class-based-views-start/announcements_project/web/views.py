# import view from django
from django.views import View
from django.shortcuts import render


class HomePageView(View):
    template_name = "web/home.html"

    # all class based view function
    # get, post, patch, delete
    # are going to take request as a param.
    def get(self, request):
        return render(
            request,
            self.template_name,
        )
