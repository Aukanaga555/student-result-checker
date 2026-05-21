from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_number=models.IntegerField()
    dob=models.DateField()
    mark=models.IntegerField()
