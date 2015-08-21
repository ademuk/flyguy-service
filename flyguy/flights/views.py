from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import Flight
from .serializers import UserSerializer, FlightSerializer


class UserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


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
