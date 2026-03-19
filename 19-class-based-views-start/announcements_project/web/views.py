# import view from django
from django.views import View
from django.shortcuts import render


class HomePageView(View):
    template_name = "web/home.html"
