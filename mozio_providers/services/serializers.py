"""The Serializers for REST API for ServiceArea."""
from rest_framework import serializers

from .models import ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):
    """Serializer based on ServiceArea Model."""

    class Meta:
        """Meta info about serializer."""

        model = ServiceArea
        fields = (
            'id', 'provider', 'name', 'price', 'polygon'
        )
