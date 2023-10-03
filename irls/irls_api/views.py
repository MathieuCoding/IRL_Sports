from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

# class EventApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     # 1. List all
#     def get(self, request, *args, **kwargs):
#         '''
#         List all the todo items for given requested user
#         '''
#         events = Event.objects.filter(user = request.user.id)
#         serializer = EventSerializer(events, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Create
#     def post(self, request, *args, **kwargs):
#         '''
#         Create the Todo with given todo data
#         '''
#         data = {
#             'name': request.data.get('name'), 
#             'date': request.data.get('date'), 
#             'user': request.user.id
#         }
#         serializer = EventSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class StructureApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     # 1. List all
#     def get(self, request, *args, **kwargs):
#         '''
#         List all the todo items for given requested user
#         '''
#         structures = Structure.objects.filter(event = request.event.id)
#         serializer = StructureSerializer(structures, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Create
#     def post(self, request, *args, **kwargs):
#         '''
#         Create the Todo with given todo data
#         '''
#         data = {
#             'city': request.data.get('city'), 
#             'name': request.data.get('name'),
#             'address': request.data.get('address')
#         }
#         serializer = EventSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)