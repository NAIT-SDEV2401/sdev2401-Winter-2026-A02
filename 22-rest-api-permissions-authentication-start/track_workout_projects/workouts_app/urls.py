from django.urls import path

# import routers from rest framework
from rest_framework.routers import DefaultRouter

from .views import ExerciseAPIView, WorkoutViewSet

# this is going to specify the urls
# for the detail and not detailed views
router = DefaultRouter()
router.register(r"workouts", WorkoutViewSet)

urlpatterns = [
    path("exercises/", ExerciseAPIView.as_view(), name="exercise-api"),
    path("exercises/<int:id>/", ExerciseAPIView.as_view(), name="exercise-detail"),
] + router.urls  # adding to the urls.
