from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    physics_marks = models.IntegerField()
    chemistry_marks = models.IntegerField()
    maths_marks = models.IntegerField()
    computer_science_marks = models.IntegerField()
