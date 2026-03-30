from django.urls import path

# just like we've done for the course
# create a url mapping to our view.
from .views import ExerciseAPIView

urlpatterns = [
    # the path that will be used to create new exercises
    # and list all exercises
    path(
        "exercise/",
        ExerciseAPIView.as_view(),
        name="exercise-api",
    ),
    # we're goign to use the same path but with an id
    # where we're going get the detail
    # update the instance
    # delete the instance.
    path(
        "exercise/<int:id>/",
        ExerciseAPIView.as_view(),
        name="exercise-api",
    ),
]
