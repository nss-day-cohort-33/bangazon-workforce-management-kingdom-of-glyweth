from django.db import models
from django.urls import reverse

class Training_Program(models.Model):

    title = models.CharField(max_length=50)
    start_date = models.DateField(null=True, blank=True, default=None)
    end_date = models.DateField(null=True, blank=True, default=None)
    capacity = models.IntegerField()
    description = models.CharField(null=True, max_length=300)


    # class Meta:
    #     verbose_name = ("TrainingProgram")
    #     verbose_name_plural = ("TrainingPrograms")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("TrainingProgram_detail", kwargs={"pk": self.pk})
