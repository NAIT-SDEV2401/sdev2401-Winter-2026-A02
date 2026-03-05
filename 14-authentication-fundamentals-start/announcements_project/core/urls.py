from django.urls import path
# I'm going to import the LoginView and LogoutView
from django.contrib.auth.views import LoginView, LogoutView

from .views import register

urlpatterns = [
    # register endpoint from last class.
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(
        template_name="core/login.html"
    ), name="login"),
    path("logout", LogoutView.as_view(),
         name="logout")

]
