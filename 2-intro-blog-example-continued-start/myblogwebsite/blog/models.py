# Create your models here.
# our classess mapped to db tables.
from django.conf import settings
from django.db import models
from django.utils import timezone

# this class is going to be how we interact with
# the database
# 1. we create the model
# 2. we need to apply this to the database so the first thing
#    we do is python manage.py makemigrations which is going to
#    create the file to apply this database table.
# 3. we need to use python manage.py migrate to apply the table.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title