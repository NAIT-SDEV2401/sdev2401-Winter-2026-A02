from django.shortcuts import render

# Create your views here.
from django.views import View

# docs: https://docs.djangoproject.com/en/5.2/topics/class-based-views/#subclassing-generic-views
from django.views.generic import TemplateView

# let's import and use our currenttime mixin
from core.mixins import CurrentTimeMixin


# inherit from our template view here
class HomePageView(CurrentTimeMixin, TemplateView):
    template_name = "web/home.html"
    # all a template view does is render the template

    # with class class based views there's function called get_context_data
    # with this function you can modify the context
    # that's passed to the template.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # let's add a title, and description to the template
        breakpoint()
        context["title"] = "Super Cool LMS"
        context["description"] = "Our awesome LMS system that we created."
        # note context passed to template here.
        return context

    # we no longer need these lines
    # def get(self, request):
    #     return render(request, self.template_name)
