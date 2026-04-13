from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# we're going to import our new permission here.
from .permissions import IsOwnerOfResourceOrReadOnly

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
    def get_queryset(self):
        return Exercise.objects.all()

    def get(self, request, id=None):
        # detail view
        if id:
            exercise = get_object_or_404(Exercise, id=id)
            serializer = ExerciseSerializer(exercise)
            return Response(serializer.data)
        # list view
        exercises = self.get_queryset()
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
    permission_classes = [IsOwnerOfResourceOrReadOnly]

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

    # override the queryset value for the apiview
    def get_queryset(self):
        # return the list of only that users workoutlogs
        return WorkoutLog.objects.filter(user=self.request.user)

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
        workout_logs = self.get_queryset()
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

    def post(self, request):

        # get serializer class which will be
        # WorkoutLogCreateUpdateSerializer
        serializer = self.get_serializer_class()(
            data=request.data  # our raw data from the request
        )
        if serializer.is_valid():  # clean/sanitization step
            # save this to a database.
            workout_log = serializer.save(
                # we're going to add the user on save.
                user=self.request.user
            )

            # this is your money magic placement.

            # respond with a different serializer that will give
            # the detail for it.
            return Response(
                WorkoutLogReadOnlySerializer(workout_log).data,
                status=201,  # created status.
            )
        # we need to handle the errors
        return Response(
            serializer.errors,  # this triggered if not valid (above)
            status=400,  # bad request
        )

    # let's create the update methods that's going to
    # give us the ability to change a workoutlog.
    def update(self, request, id, partial=False):
        # we need to get the object
        workout_log = get_object_or_404(WorkoutLog, id=id)

        # we are updating an existing item and we only want the user to
        # be able to modify their own.
        self.check_object_permissions(
            request,  # the request
            workout_log,  # the instance that is passed.
        )

        # this is essentially being done already this is
        serializer = self.get_serializer_class()(
            workout_log,  # instance from the db you want to update
            data=request.data,  # what we want to change the instance with.
            partial=partial,  # going to make the distinction in the serializer if you're modifying
            # all the fields or just part of the fields
        )
        # is this valid
        if serializer.is_valid():
            # above calls the field validation and the cross validation.
            # we're going to save.
            updated_workout_log = serializer.save(
                user=self.request.user,
            )

            return Response(
                WorkoutLogReadOnlySerializer(updated_workout_log).data,
            )

        # errors are given from the is_valid function here.
        return Response(
            serializer.errors,
            status=400,
        )

    # full replacement of the fields in the instance
    def put(self, request, id):
        return self.update(request, id, partial=False)

    # only going to replace a few.
    def patch(self, request, id):
        return self.update(request, id, partial=True)
