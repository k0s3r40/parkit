from django.db import models


class Camera(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address_verbose = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=False, null=False)
    lat = models.CharField(max_length=255, blank=False, null=False)
    long = models.CharField(max_length=255, blank=False, null=False)
    mask = models.ImageField(upload_to='media/masks',blank=False, null=False, help_text='png mask for the camera')
    orientation = models.CharField(max_length=255, blank=False, null=False, help_text='The angle between the north and the orientation of the camera in degrees')
    max_cap = models.IntegerField(blank=False, null=False)
    current_load = models.IntegerField(blank=False, null=False)
    is_stationary = models.BooleanField()
    
    def __str__(self):
        return self.name