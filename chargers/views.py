from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from reviews.models import ChargerReview
from .models import Charger
from .serializers import ChargerSerializer
from .serializers import ChargerSearchSerializer

from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

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

class ChargerSearchViewSet(viewsets.ModelViewSet):
    serializer_class = ChargerSearchSerializer
    def list(self, request, *args, **kwargs):
        statNm = request.query_params.get("statNm", None)
        if statNm is not None:
            charger = Charger.objects.filter(statNm__contains=statNm)
            if not charger:
                return Response({"status": "statNm do not exits"},
                                status=status.HTTP_400_BAD_REQUEST)
            serializer = ChargerSearchSerializer(data=charger, many=True)
            serializer.is_valid(raise_exception=False)
            return Response(serializer.data)
        serializer = ChargerReviewSerializer(data=self.get_queryset(statNm),
                                             many=True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data)
       

    def get_queryset(self):
        return Charger.objects.all()
