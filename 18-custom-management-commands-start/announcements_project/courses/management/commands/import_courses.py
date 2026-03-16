# this is our management command.
# import csv to use it
import csv

# create the command with an argument
from django.core.management.base import BaseCommand

# here we're importing the course using
# a non relative import.
from courses.models import Course


class Command(BaseCommand):
    help = "Import courses from a csv file."

    # let's add an argument that will be the file path
    # of the csv file.
    def add_arguments(self, parser):
        # add the csv argument
        parser.add_argument(
            "csv_file",  # the name of the argument
            type=str,
            help="csv file path to import.",
        )

    # these might take a flexible number of arguments
    # args: is a list of positional arguments passed in.
    # kwargs: is a dictionary of named arguments passed in.

    def handle(self, *args, **kwargs):
        # get the csv_file from the kwargs
        csv_file = kwargs.get("csv_file")
        # we're going to check if the file was passed in
        # show an error if not.
        if not csv_file:
            self.stdout.write(
                self.style.ERROR(
                    "Please provide a csv",
                )
            )

        # we are going to parse that file
        # create course instances.
        with open(csv_file, newline="") as file:
            reader = csv.DictReader(file)
            # all rows will take this format
            # {'title': '...', 'description': '...'}
            count = 0
            for row in reader:
                course, created = Course.objects.get_or_create(
                    title=row.get("title"),
                    description=row.get("description"),
                )
                if created:
                    count += 1

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully import {count} courses.",
                )
            )
