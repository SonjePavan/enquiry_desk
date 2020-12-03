from django.db import models


# Create your models here.
class StudentData(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    mobile_number = models.IntegerField()
    address = models.TextField(max_length=200)
    course=models.TextField(max_length=100)
    timendate=models.TextField(max_length=100)
    extra=models.TextField(max_length=10)

    def __str__(self):
        return self.firstname
