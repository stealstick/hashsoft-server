from rest_framework import viewsets

from .models import Board, Dataroom
from .serializers import BoardSerializer, DataroomSerializer


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()

class DataroomViewSet(viewsets.ModelViewSet):
    serializer_class = DataroomSerializer
    queryset = Dataroom.objects.all()
