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
