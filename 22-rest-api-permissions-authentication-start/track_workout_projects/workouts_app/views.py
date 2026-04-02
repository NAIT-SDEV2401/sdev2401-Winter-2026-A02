from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

# we're going to import viewsets which
# simplify the creation of a APIView
from rest_framework import viewsets

from .serializers import (
    ExerciseSerializer,
    WorkoutSerializer,
)

# import Workout from the models
from .models import Exercise, Workout


class ExerciseAPIView(APIView):

    def get(self, request, id=None):
        # detail view
        if id:
            exercise = get_object_or_404(Exercise, id=id)
            serializer = ExerciseSerializer(exercise)
            return Response(serializer.data)
        # list view
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            exercise = serializer.save()
            # this will call the create method internally.
            return Response(ExerciseSerializer(exercise).data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, id, partial=False):
        exercise = get_object_or_404(Exercise, id=id)
        serializer = ExerciseSerializer(exercise, data=request.data, partial=partial)
        if serializer.is_valid():
            exercise = serializer.save()
            return Response(ExerciseSerializer(exercise).data)
        return Response(serializer.errors, status=400)

    # we can use the same update function for both PUT and PATCH requests by passing in the partial argument
    def put(self, request, id):
        return self.update(request, id, partial=False)

    def patch(self, request, id):
        return self.update(request, id, partial=True)

    def delete(self, request, id):
        exercise = get_object_or_404(Exercise, id=id)
        exercise.delete()
        return Response(status=204)


class WorkoutViewSet(viewsets.ModelViewSet):
    # queryset (what is fetched from the db)
    queryset = Workout.objects.all()
    # note you can use get_queryset instead
    # if you want to filter based on the
    # user from the request.
    serializer_class = WorkoutSerializer
