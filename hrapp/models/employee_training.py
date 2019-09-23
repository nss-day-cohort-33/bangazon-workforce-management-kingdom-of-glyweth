from django.db import models
from .employee import Employee
from .training_program import Training_Program

class Training_Program_Employee(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training_program = models.ForeignKey(Training_Program, on_delete=models.CASCADE)