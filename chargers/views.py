from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import ChargerSerializer
from .models import Charger
from reviews.models import ChargerReview


class ChargerViewSet(viewsets.ModelViewSet):
    serializer_class = ChargerSerializer
    queryset = Charger.objects.all()
    lookup_field = 'statId'


    @detail_route(methods=['GET'])
    def reviews(self, request, statId=None):
        try:
            charger = Charger.objects.get(statId=statId)
        except:
            return Response({"status": "fail"},
                            status=status.HTTP_400_BAD_REQUEST)
        chargerReview = ChargerReview.objects.filter(charger=charger)
        return Response(chargerReview)
