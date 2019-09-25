from django.db import models
# from django.urls import reverse


class Computer(models.Model):
    # '''
    # description: This class creates a computer and its properties
    # author: Joe Shep
    # properties:
    #   make: The make will contain the name of the brand of the computer.
    #   purchase_date: This property contains the purchase date in string form.
    #   decomission_date: This property contains the dicomission date in string form.
    #   employees: This property contains the many to many relationship with the computer/employee model
    # '''

    manufacturer = models.CharField(null=True, max_length=25)
    model = models.CharField(null=True, max_length=25)
    purchase_date = models.DateField()
    decommission_date = models.DateField(null=True, blank=True, default=None)


