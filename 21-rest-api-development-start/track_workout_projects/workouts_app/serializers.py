# this file will be in all of your DRF apps
# hold the serializers which
# convert items to json or parse the json.

from rest_framework import serializers

from .models import Exercise


# serializing the model of exercise
class ExerciseSerializer(serializers.Serializer):
    # id is on every model and is handled
    # by the db, this is why it's read_only
    id = serializers.IntegerField(read_only=True)
    # fields
    name = serializers.CharField(max_length=100)
    # this is going to have the same restriction
    # as the database model field
    exercise_type = serializers.ChoiceField(
        choices=Exercise.EXERCISE_TYPES,
    )
