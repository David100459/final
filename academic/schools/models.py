from django.db import models

# Create your models here.

class student(models.Model) :
    firt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField()

class subject(models.Model) :
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    course = models.CharField(max_length=3)
    created_at = models.DateTimeField()

class subject2(models.Model) :
    id_student = models.ForeignKey(student, on_delete=models.CASCADE)
    id_subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
