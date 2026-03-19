from django.core.management.base import BaseCommand
from django.core.mail import send_mail

from courses.models import Submission


# I want a management command
class Command(BaseCommand):
    # help of "notify instructors about new submissions"
    help = "notify instructors about new submissions"

    # no arguments

    # inside of the handle (what's executed)
    def handle(self, *args, **kwargs):
        # fetch all submissions that have instructor_notified
        # of false
        new_submissions = Submission.objects.filter(
            instructor_notified=False,
        )
        # count them
        new_submissions.count()
        # loop through the submissions
        for submission in new_submissions:
            # get the instructor owner
            instructor = submission.assignment.owner
            breakpoint()
            # send an email with send_mail from django
            # set the instrcutor_notified to true.
            # give a message, telling the user how many they've
            # sent.
