from rest_framework import permissions, viewsets
from .models import Event, Structure, Sport, User
from .serializers import EventSerializer, StructureSerializer, SportSerializer, UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('created_date')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class StructureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer
    permission_classes = [permissions.IsAuthenticated]

class SportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
