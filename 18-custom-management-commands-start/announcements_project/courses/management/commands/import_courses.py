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

    def handle(self, *args, **kwargs):
        print("hello import los csv!")
        breakpoint()
