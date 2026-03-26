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
    def get(self, request):
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
