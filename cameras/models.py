import math

from django.db import models


def compute_crds(rotation: int, lat: str, long: str, distance: float = -0.001):
    R = 6378.1
    brng = math.radians(rotation / math.pi)
    d = distance

    lat1 = math.radians(float(lat))
    lon1 = math.radians(float(long))
    lat2 = math.asin(math.sin(lat1) * math.cos(d / R) + math.cos(lat1) * math.sin(d / R) * math.cos(brng))
    lon2 = lon1 + math.atan2(math.sin(brng) * math.sin(d / R) * math.cos(lat1), math.cos(d / R) - math.sin(lat1) * math.sin(lat2))

    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)

    return {
        'lat': str(lat2),
        'long': str(lon2)
    }


class Camera(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address_verbose = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=False, null=False)
    lat = models.CharField(max_length=255, blank=False, null=False)
    long = models.CharField(max_length=255, blank=False, null=False)
    mask = models.ImageField(upload_to='media/masks', blank=False, null=False, help_text='png mask for the camera')
    orientation = models.CharField(max_length=255, blank=False, null=False, help_text='The angle between the north and the orientation of the camera in degrees')
    max_cap = models.IntegerField(blank=False, null=False)
    current_load = models.IntegerField(blank=False, null=False)
    is_stationary = models.BooleanField()
    area_width = models.FloatField(default=0)
    area_height = models.FloatField(default=0)

    def __str__(self):
        return self.name

    @property
    def pins(self):
        base = compute_crds(rotation=int(self.orientation), lat=self.lat, long=self.long)
        f = [base]
        new_ff = []
        if self.is_stationary:
            for i in range(self.max_cap-self.current_load):
                d = (1 / 1000) * 3
                f.append(compute_crds(distance=-d,rotation=int(self.orientation), lat=f[-1]['lat'], long=f[-1]['long']))
        else:
            for i in range(1,10):
                d = (i/1000)*3
                ff = compute_crds(distance=d,rotation=int(self.orientation), lat=base['lat'], long=base['long'])
                f.append(ff)
                print(int(self.orientation))
            for i in f:
                ff = compute_crds(distance=-0.01,rotation=int(350), lat=i['lat'], long=i['long'])
                new_ff.append(ff)
            for i in f:
                ff = compute_crds(distance=-0.02, rotation=int(350), lat=i['lat'], long=i['long'])
                new_ff.append(ff)
            # for i in f:
            #     ff = compute_crds(distance=0.02, rotation=int(350), lat=i['lat'], long=i['long'])
            #     new_ff.append(ff)




        return f+new_ff

