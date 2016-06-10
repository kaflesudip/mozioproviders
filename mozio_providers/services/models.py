from django.contrib.gis.db import models
from mozio_providers.providers.models import Provider


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    polygon = models.PolygonField()
