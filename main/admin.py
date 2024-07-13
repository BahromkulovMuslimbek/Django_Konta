from django.contrib import admin
from . import models

admin.site.register(models.Contact)
admin.site.register(models.Teacher)
admin.site.register(models.Courses)
admin.site.register(models.OurStudentsSay)
admin.site.register(models.CoursesCategories)