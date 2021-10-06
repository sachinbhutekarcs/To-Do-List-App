from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(unique=True, max_length=264)
    status = models.BooleanField()

    def __str__(self):
        return self.name
