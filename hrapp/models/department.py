from django.db import models

class Department(models.Model):

    name = models.CharField(max_length=25)
    #change to decimal in the future
    budget = models.models.DecimalField(decimal_places=2)