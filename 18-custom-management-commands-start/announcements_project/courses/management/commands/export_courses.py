# I want you to create a management command
# that takes a single argument "output_file"
# that will take all of the courses (in our db.)
# write a csv file in the output file.
import csv

from django.core.management.base import BaseCommand

from courses.models import Course


class Command(BaseCommand):
    help = "Export courses to a csv file"

    def add_arguments(self, parser):
        parser.add_argument(
            "output_file",
            type=str,
            help="Output of content for courses",
        )

    def handle(self, *args, **kwargs):
        # get the output file
        output_file = kwargs.get("output_file")
        if not output_file:
            self.stdout.write(
                self.style.ERROR("Please provide output file."),
            )
            # early return
            return

        # get all courses
        courses = Course.objects.all()
        # write the file.
        # mode="w" means write
        with open(output_file, mode="w", newline="") as file:
            # create a csv writer
            writer = csv.writer(file)
            # let's add the heading
            writer.writerow(["course title", "course description"])
            # loop through courses and add their title and description
            for course in courses:
                writer.writerow([course.title, course.description])

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully exported {courses.count()} to {output_file}"
                )
            )
