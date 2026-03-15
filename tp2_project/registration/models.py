from django.db import models

# Create your models here.
class Student(models.Model):
    S_name=models.CharField(max_length=100)
    S_DOB=models.DateField()

    def __str__(self):
        return self.S_name

class Course(models.Model):
    C_name=models.CharField(max_length=100)
    C_credits=models.CharField(max_length=10)

    def __str__(self):
        return self.C_name

class Register(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    R_date=models.DateField()

    def __str__(self):
        return f"{self.student} - {self.course}"