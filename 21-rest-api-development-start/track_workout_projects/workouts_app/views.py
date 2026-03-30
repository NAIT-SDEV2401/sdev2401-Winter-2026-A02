from django.shortcuts import get_object_or_404

# import the APIView (which is like the View class in django)
from rest_framework.views import APIView

# import the response which acts like render
# except it'll respond with json
from rest_framework.response import Response

# we're going to import our own classes
from .serializers import ExerciseSerializer
from .models import Exercise


class ExerciseAPIView(APIView):
    # this is normally what you
    # can use to access the database
    # items
    def get_queryset(self):
        return Exercise.objects.all()

    # request method for get
    # looks a lot like a class based view in django
    # specify the id parameter with a default value of None
    def get(self, request, id=None):
        # detail view
        # check that the id is not noe
        if id is not None:
            # get the single exercise from the db.
            exercise = get_object_or_404(Exercise, id=id)
            # serialize the single instance from the db
            serializer = ExerciseSerializer(exercise)
            # respond with the single item.
            return Response(serializer.data)

        # below is the list.

        # getting them from the database.
        exercises = self.get_queryset()
        # i'm going serialize the data
        serializer = ExerciseSerializer(
            exercises,  # model instances
            many=True,  # because there's more than one.
        )
        # return the response of the serializer data
        return Response(serializer.data)

    # add a post request.
    def post(self, request):
        # deserialize the data
        # as part of the request
        # we're going to send json as part
        # of the body here we're making it readable
        # in python
        serializer = ExerciseSerializer(
            data=request.data,
        )
        # just like a form we need to check if it's
        # valid.
        if serializer.is_valid():
            # we're going to create the instance
            # save here will call our create
            # inside of our serializer
            exercise = serializer.save()  # returns a db instance
            # then we're going to render the db instance
            return Response(
                ExerciseSerializer(exercise).data,
            )
        # if it's not valid
        return Response(
            serializer.errors,
            status=400,  # there's an error in the request.
        )

    # update for put and patch
    def update(self, request, id, partial=False):
        # what do I need to do here.
        exercise = get_object_or_404(Exercise, id=id)
        # pass an instance in the form. (pass the partial into the form.)
        serializer = ExerciseSerializer(
            exercise,
            data=request.data,
            partial=partial,
        )
        # if it's valid
        if serializer.is_valid():
            # save the data
            updated_exercise = serializer.save()  # returns an instance
            # this calls update under the hood.
            return Response(ExerciseSerializer(updated_exercise).data)
        # return a response
        return Response(
            serializer.errors,
            status=400,
        )

    def put(self, request, id):
        self.update(request, id, partial=False)

    def patch(self, request, id):
        self.update(request, id, partial=True)
