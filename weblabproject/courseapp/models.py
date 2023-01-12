from django.db import models

# Create your models here.
class Course (models.Model):
    course_id= models.CharField(max_length=20)
    course_name= models.CharField(max_length=45)
    course_credit= models.DecimalField(decimal_places=2,max_length=10,max_digits=5, verbose_name='Course Credit: ')
    ct_full_marks= models.DecimalField(decimal_places=2,max_digits=5,max_length=10)
    att_full_marks= models.DecimalField(decimal_places=2,max_digits=5,max_length=10)
    final_full_marks= models.DecimalField(decimal_places=2,max_digits=5,max_length=10) 
