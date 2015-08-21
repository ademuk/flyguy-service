from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Flight


class UserSerializer(serializers.ModelSerializer):
    flights = serializers.PrimaryKeyRelatedField(many=True, queryset=Flight.objects.all())

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'flights')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
    	User = get_user_model()
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class FlightSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Flight
        fields = ('id', 'url', 'name', 'date', 'notes', 'owner')
