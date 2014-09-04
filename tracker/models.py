from django.db import models
from django.contrib.auth.models import User


class BaseModelDate(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(BaseModelDate):
    created_by = models.ForeignKey(User)
    name = models.CharField(max_length=250, null=True, blank=True)
    assigneds = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.name


class Folder(BaseModelDate):
    created_by = models.ForeignKey(User)
    parent = models.ForeignKey('self', null=True, blank=True)
    code = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    order = models.CommaSeparatedIntegerField(default=0)
    assigneds = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.code


class TaskToUser(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey('Task')


class Task(BaseModelDate):
    created_by = models.ForeignKey('User')
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    expected_finish_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(auto_now=True)

    owners = models.ManyToManyField('self', through=TaskToUser)
    assigneds = models.ManyToManyField('self', null=True, blank=True, through=TaskToUser)
    approvals = models.ManyToManyField('self', null=True, blank=True, through=TaskToUser)
    stackholders = models.ManyToManyField('self', null=True, blank=True, through=TaskToUser)

    def __str__(self):
        return self.title


class TaskDependency(BaseModelDate):
    # This reference points to a Task that needs some other Task to be concluded.
    dependent_task = models.ForeignKey(Task, related_name='dependent_task')
    # This, in turn, points to the specific Task that is holding the conclusion of another one.
    depends_on = models.ForeignKey(Task, related_name='depends_on')

    def save(self):
        if self.dependent_task == self.depends_on:
            raise AttributeError('A Task cannot depend on itself.')


class Comment(BaseModelDate):
    parent = models.ForeignKey('self', null=True, blank=True)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)

    def __str__(self):
        return self.title
