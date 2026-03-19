from django.urls import path

from .views import HomePageView

urlpatterns = [
    path(
        "",
        HomePageView.as_view(),  # as_view is needed for cbvs
        name="home",
    )
]
