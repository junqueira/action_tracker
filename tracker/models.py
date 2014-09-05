from django.db import models
from django.contrib.auth.models import User


class BaseModelDate(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(BaseModelDate):
    created_by = models.ForeignKey(User, related_name='project_creted_by')
    name = models.CharField(max_length=250, null=True, blank=True)
    project_assigneds = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.name


class Folder(BaseModelDate):
    created_by = models.ForeignKey(User, related_name='folder_creted_by')
    parent = models.ForeignKey('self', null=True, blank=True)
    code = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    order = models.IntegerField(default=0)
    folder_assigneds = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.code


class Task(BaseModelDate):
    created_by = models.ForeignKey(User, related_name='task_creted_by')
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    expected_finish_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(auto_now=True)

    task_owners = models.ManyToManyField(User, related_name='task_owners')
    task_assigneds = models.ManyToManyField(User, null=True, blank=True,
                                            related_name='task_assigneds')
    task_approvals = models.ManyToManyField(User, null=True, blank=True,
                                            related_name='task_approvals')
    task_stackholders = models.ManyToManyField(User, null=True, blank=True,
                                               related_name='task_stackholders')

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
