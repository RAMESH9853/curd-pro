from django.db import models

class EmpData(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.BigIntegerField()
    company = models.CharField(max_length=100)
    salary = models.BigIntegerField()
    location = models.CharField(max_length=100)

