"""Models related to ServiceArea."""
from django.contrib.gis.db import models
from mozio_providers.providers.models import Provider


class ServiceArea(models.Model):
    """This model stores information of a area and its polygon."""

    provider = models.ForeignKey(Provider)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    polygon = models.PolygonField()

    def __str__(self):
        """Default value to return."""
        return self.name
