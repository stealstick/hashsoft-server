from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from reviews.models import ChargerReview
from .models import Charger
from .serializers import ChargerSerializer


class ChargerViewSet(viewsets.ModelViewSet):
    serializer_class = ChargerSerializer
    queryset = Charger.objects.all()
    lookup_field = 'statId'


    @detail_route(methods=['GET'])
    def reviews(self, request, statId=None):
        try:
            charger = Charger.objects.filter(statId=statId)[0]
        except:
            return Response({"status": "fail"},
                            status=status.HTTP_400_BAD_REQUEST)
        chargerReview = ChargerReview.objects.filter(charger=charger)
        return Response(chargerReview)
