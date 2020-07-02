from django.db import models
from uuid import uuid4

# Create your models here.

class Bank(models.Model):
    bank_name = models.CharField(max_length=40)
    bank_id = models.IntegerField()
    ifsc = models.CharField(max_length=11)
    city = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.bank_name + "->" + self.district + "->" + self.branch

# class Bank(models.Model):
#     ifsc = models.TextField()
#     bank_id = models.IntegerField()
#     branch = models.TextField()
#     address = models.TextField()
#     city = models.TextField()
#     district = models.TextField()
#     state = models.TextField()
#     bank_name = models.TextField()
