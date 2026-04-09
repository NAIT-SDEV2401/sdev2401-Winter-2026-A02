from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .serializers import (
    ExerciseSerializer,
    WorkoutSerializer,
    WorkoutLogCreateUpdateSerializer,
    WorkoutLogReadOnlySerializer,
)
from .models import Exercise, Workout, WorkoutLog


class WorkoutViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


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


class WorkoutLogAPIView(APIView):
    # permissions
    permissions_classes = [IsAuthenticated]

    # override the default serializer_class and make it
    # change based on the type of request that we
    # are using
    def get_serializer_class(self):
        # if it's a create we're going to return
        # the proper serializer
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return WorkoutLogCreateUpdateSerializer
        # otherwise "GET"
        return WorkoutLogReadOnlySerializer

    # this will be used for both detail and list.
    def get(self, request, id=None):
        # detail view
        if id:
            workout_log = get_object_or_404(WorkoutLog, id=id)
            # this is equivalent to WorkoutLog.objects.get(id=id)
            # except it returns a 404 if not there.
            serializer = self.get_serializer_class()(workout_log)
            # this is a single above.
            return Response(serializer.data)

        # list view
        workout_logs = WorkoutLog.objects.all()
        # we're going to use our new class to serialize
        # the data since it's get it will use the
        # WorkoutLogReadOnlySerializer
        # which is returned from self.get_serializer_class()
        # We're initializing the class immediately.
        serializer = self.get_serializer_class()(
            workout_logs,
            many=True,  # this because it's a queryset.
        )
        return Response(serializer.data)
