import csv

from django.db import models
from django.conf import settings
from django.utils import timezone


# create an assignment
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assingments",
    )

    def __str__(self):
        return self.title

    # the cls on a class method is the class itself
    # we won't be using it.
    @classmethod
    def create_assignments_from_csv(cls, csv_file, owner):
        # decode the csv
        decoded_file = csv_file.read().decode("utf-8").splitlines()
        # dictreader
        reader = csv.DictReader(decoded_file)
        assignments = []

        # loop through the csv
        for row in reader:
            # a row will have data like this:
            # {'title': 'Assignment 1', 'description': 'Introduction to Python', 'date': '2026-02-10', 'time': '09:00'}
            # create assignment
            new_assignment, created = Assignment.objects.get_or_create(
                title=row.get("title"),
                description=row.get("description"),
                due_date=timezone.now(),
                owner=owner,
            )
            # keep track of assignments
            if created:
                assignments.append(new_assignment)

        # return assignments created.
        return assignments


# create a submission
class Submission(models.Model):
    # - assignment foreign key to assignment cascade.
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name="submission",
    )
    # - student_name that's just a charfield
    student_name = models.CharField(max_length=100)
    # - file filefield that uploads to "submissions/"
    file = models.FileField(
        upload_to="submissions/",
    )
    # - submitted_at datetime fileld when the item was created.
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.student_name} for {self.assignment}"
