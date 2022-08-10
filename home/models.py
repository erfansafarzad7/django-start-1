from django.db import models


class Todo (models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    c_time = models.DateTimeField()
