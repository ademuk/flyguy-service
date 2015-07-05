from .models import Flight
from rest_framework import viewsets
from .serializers import FlightSerializer


class FlightViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows flights to be viewed or edited.
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get_queryset(self):
        """
        This view returns a list of all the flights
        for the currently authenticated user.
        """
        user = self.request.user
        return Flight.objects.filter(owner=user)

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)
