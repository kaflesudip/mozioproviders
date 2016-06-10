"""View to provide REST API for ServiceArea."""
from rest_framework import generics

from django.contrib.gis.geos import Point

from .models import ServiceArea
from .serializers import ServiceAreaSerializer


class ServiceAreaCollection(generics.ListAPIView):
"""Lists all Services in which the point lies within the given polygon."""
    serializer_class = ServiceAreaSerializer

    def get_queryset(self):
        lat = float(self.kwargs.get('lat'))
        lon = float(self.kwargs.get('lon'))
        point = Point(lon, lat)
        return ServiceArea.objects.filter(polygon__contains=point)


class ServiceAreaCreate(generics.ListCreateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaMember(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
