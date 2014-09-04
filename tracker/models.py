from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    #log fields
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    #business fields
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    expected_finish_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(auto_now=True)


class TaskOwner(models.Model):
    #log fields
    creation_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)


class TaskAssignedTo(models.Model):
    #log fields
    creation_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)


class TaskDependency(models.Model):
    #log fields
    creation_date = models.DateTimeField(auto_now_add=True)

    # This reference points to a Task that needs some other Task to be concluded.
    dependent_task = models.ForeignKey(Task, related_name='dependent_task')
    # This, in turn, points to the specific Task that is holding the conclusion of another one.
    depends_on = models.ForeignKey(Task, related_name='depends_on')
