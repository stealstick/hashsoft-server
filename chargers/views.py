from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from reviews.models import ChargerReview
from .models import Charger
from .serializers import ChargerSerializer
from .serializers import ChargerSimpleSerializer
from .serializers import ChargerSearchSerializer

from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

class ChargerViewSet(viewsets.ModelViewSet):
    serializer_class = ChargerSerializer
    queryset = Charger.objects.all()
    lookup_field = 'pk'


    @detail_route(methods=['GET'])
    def reviews(self, request, sid=None):
        try:
            charger = Charger.objects.filter(sid=sid)[0]
        except:
            return Response({"status": "fail"},
                            status=status.HTTP_400_BAD_REQUEST)
        chargerReview = ChargerReview.objects.filter(charger=charger)
        return Response(chargerReview)

class Charger2ViewSet(viewsets.ModelViewSet):
    serializer_class = ChargerSerializer
    queryset = Charger.objects.all()
    lookup_field = 'pk'


    @detail_route(methods=['GET'])
    def reviews(self, request, sid=None):
        try:
            charger = Charger.objects.filter(sid=sid)[0]
        except:
            return Response({"status": "fail"},
                            status=status.HTTP_400_BAD_REQUEST)
        chargerReview = ChargerReview.objects.filter(charger=charger)
        return Response(chargerReview)

class ChargerClearViewSet(viewsets.ModelViewSet):
    serializer_class = ChargerSimpleSerializer
    queryset = Charger.objects.values('sid', 'stat')

class ChargerSearchViewSet(viewsets.ModelViewSet):
    serializer_class = ChargerSearchSerializer
    def list(self, request, *args, **kwargs):
        name = request.query_params.get("name", None)
        if  name is not None:
            charger = Charger.objects.filter(name__contains= name)
            if not charger:
                return Response({"status": " name do not exits"},
                                status=status.HTTP_400_BAD_REQUEST)
            serializer = ChargerSearchSerializer(data=charger, many=True)
            serializer.is_valid(raise_exception=False)
            return Response(serializer.data)
        serializer = ChargerReviewSerializer(data=self.get_queryset( name),
                                             many=True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data)
       

    def get_queryset(self):
        return Charger.objects.all()
