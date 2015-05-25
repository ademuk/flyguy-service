from .models import Flight
from rest_framework import serializers


class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = ('url', 'name', 'date', 'notes')
