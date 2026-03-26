from django.urls import path

# just like we've done for the course
# create a url mapping to our view.
from .views import ExerciseAPIView

urlpatterns = [
    path(
        "execise/",
        ExerciseAPIView.as_view(),
        name="exercise-api",
    ),
]
