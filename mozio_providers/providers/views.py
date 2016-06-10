"""API for providers."""
from rest_framework import generics

from .models import Provider
from .serializers import ProviderSerializer


class ProviderCollection(generics.ListCreateAPIView):
    """API that lists all Poviders on GET, Creates new on POST request."""

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderMember(generics.RetrieveUpdateDestroyAPIView):
    """API that lists, updates or deletes single provider on GET, PUT or DELETE request respectively."""

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
