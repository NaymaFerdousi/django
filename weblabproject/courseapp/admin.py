from django.contrib import admin

#from .models import Course
from . import models


# Register your models here.

#admin.site.register(Course) 
admin.site.register(models.Course)
