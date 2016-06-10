from rest_framework import generics

from django.contrib.gis.geos import Point

from .models import ServiceArea
from .serializers import ServiceAreaSerializer


class ServiceAreaCollection(generics.ListAPIView):
    serializer_class = ServiceAreaSerializer

    def get_queryset(self, lat, lon):
        point = Point(lat, lon)
        return ServiceArea.objects.filter(polygon__contains=point)


class ServiceAreaCreate(generics.ListAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


# class ProviderMember(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer
