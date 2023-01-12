from django.db import models

# Create your models here.


class Program(models.Model):
    pg_name = models.CharField(max_length=30)

    def __str__(self):
        return self.pg_name

class Student(models.Model):
    st_id = models.PositiveSmallIntegerField()
    st_name = models.CharField(max_length=25)
    st_dob = models.DateField()
    st_dist = models.CharField(max_length=15)
    st_phone = models.CharField(max_length=11)
    st_mail = models.EmailField()
    pg_name = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.st_id)