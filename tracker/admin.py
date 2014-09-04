from django.contrib import admin
from .models import Folder, Project, Task, Comment

admin.site.register(Folder)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comment)
