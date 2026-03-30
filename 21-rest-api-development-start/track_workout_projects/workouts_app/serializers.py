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

    # using your knowledge of forms and also some of the slides here
    # try to validate name
    # so that it can't be "sitting", "eating", "lying down"
    # raise a validation error if it is

    # on a serializer it has the same functions
    # as a form.
    # there's a function called save
    # that will either call create if it's new
    # or update if it's an existing instance

    def create(self, validated_data):
        # take our validated data
        # is a dictionary of values of name, exercise_type
        # and create an item.
        return Exercise.objects.create(
            **validated_data,
        )

    # let's create the instance on save.
    def update(self, instance, validated_data):
        # update the instance with either validated data or
        # the existing value and then save the instance.
        instance.name = validated_data.get("name", instance.name)
        instance.exercise_type = validated_data.get(
            "exercise_type", instance.exercise_type
        )
        instance.save()
        return instance
