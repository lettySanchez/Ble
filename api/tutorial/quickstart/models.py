from django.db import models
from django.db import IntegrityError
# Create your models here.
class Beacon(models.Model):
    last_seen = models.DateTimeField()
    name = models.CharField(max_length = 200, null = True)
    beacon_id = models.CharField(max_length=200, null = True)
    tractor_id = models.CharField(max_length=200, null = True)
    implement_id = models.CharField(max_length=200, null = True)
    longitude = models.CharField(max_length=200, null = True)
    latitude = models.CharField(max_length=200, null = True)

    def __unicode__(self):
        return '{} {} {}'.format(self.beacon_id, self.name, self.last_seen,
                                 self.tractor_id, self.implement_id,
                                 self.longitude, self.latitude)
