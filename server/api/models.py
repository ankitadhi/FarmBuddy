# models.py
from django.db import models
from django.db.models import JSONField


class Crop(models.Model):
    name = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=200)
    pH_range = models.CharField(max_length=50)
    growing_period = models.CharField(max_length=50,
                                      default="Not specified",  # Add default here
                                      null=False,)

    def __str__(self):
        return self.name


class Disease(models.Model):
    # Using the provided ID format
    id = models.CharField(max_length=100, primary_key=True)
    crop = models.ForeignKey(
        Crop, related_name='diseases', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    remedies = JSONField()  # Stores list of remedies

    def __str__(self):
        return f"{self.crop.name} - {self.name}"


class Step(models.Model):
    crop = models.ForeignKey(Crop, related_name='steps',
                             on_delete=models.CASCADE)
    step = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    details = JSONField()  # Stores all step details as JSON

    class Meta:
        ordering = ['step']

    def __str__(self):
        return f"{self.crop.name} - Step {self.step}: {self.title}"
