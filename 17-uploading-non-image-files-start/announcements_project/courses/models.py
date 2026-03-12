from django.db import models
from django.conf import settings


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
