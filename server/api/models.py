from django.db import models


class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    soil_type = models.CharField(max_length=255)
    pH_range = models.CharField(max_length=50)
    planting_depth = models.CharField(max_length=50, blank=True, null=True)
    spacing = models.CharField(max_length=100, blank=True, null=True)
    growing_period = models.CharField(max_length=50, blank=True, null=True)
    water_requirements = models.TextField()
    fertilization = models.TextField()
    common_diseases = models.TextField()
    common_pests = models.TextField()
    harvesting_details = models.TextField()

    def __str__(self):
        return self.name
