from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.department_name


class Employee(models.Model):
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'De naam is {self.first_name} {self.last_name}'
