from django.contrib import admin

from exam import models

# Register your models here.
admin.site.register(models.Question)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Course)


def __str__(self):
    return self.realname