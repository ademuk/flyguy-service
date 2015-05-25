from .models import Flight
from rest_framework import viewsets
from .serializers import FlightSerializer


class FlightViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows flights to be viewed or edited.
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
