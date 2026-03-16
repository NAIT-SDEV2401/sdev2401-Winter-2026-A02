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

    def handle(self, *args, **kwargs):
        print("hello import los csv.!")
