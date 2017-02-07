
from rest_framework import viewsets
from .serializers import ChargerSerializer
from .models import Charger


class ChargerViewSet(viewsets.ModelViewSet):
    serializer_class = ChargerSerializer
    queryset = Charger.objects.all()
    lookup_field = 'statId'
