from rest_framework import viewsets

from .models import Caveat
from .serializers import CaveatSerializer


class CaveatViewSet(viewsets.ModelViewSet):
    serializer_class = CaveatSerializer
    queryset = Caveat.objects.all()
