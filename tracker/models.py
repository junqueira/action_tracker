from django.db import models

class Task(models.Model):
    #log fields
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    #business fields
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    expected_finish_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(auto_now=True)
