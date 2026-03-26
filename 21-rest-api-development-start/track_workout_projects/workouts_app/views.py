# import the APIView (which is like the View class in django)
from rest_framework.views import APIView

# import the response which acts like render
# except it'll respond with json
from rest_framework.response import Response

# we're going to import our own classes
from .serializers import ExerciseSerializer
from .models import Exercise


class ExerciseAPIView(APIView):
    # request method for get
    # looks a lot like a class based view in django
    def get(self, request):
        # getting them from the database.
        exercises = Exercise.objects.all()
        # i'm going serialize the data
        serializer = ExerciseSerializer(
            exercises,  # model instances
            many=True,  # because there's more than one.
        )
        # return the response of the serializer data
        return Response(serializer.data)
