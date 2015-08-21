from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Flight


class UserSerializer(serializers.ModelSerializer):
    flights = serializers.PrimaryKeyRelatedField(many=True, queryset=Flight.objects.all())

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'flights')

class FlightSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Flight
        fields = ('id', 'url', 'name', 'date', 'notes', 'owner')
