from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from chargers.models import Charger
from .models import ChargerReview
from .serializers import ChargerReviewSerializer


class ChargerReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ChargerReviewSerializer

    def list(self, request, *args, **kwargs):
        statId = request.query_params.get("statId", None)
        if statId is not None:
            charger = Charger.objects.filter(statId=statId)[0]
            if not charger:
                return Response({"status": "statId do not exits"},
                                status=status.HTTP_400_BAD_REQUEST)
                reviews = ChargerReview.objects.filter(charger=charger)
                serializer = ChargerReviewSerializer(data=reviews, many=True)
                serializer.is_valid(raise_exception=False)
                return Response(serializer.data)
        serializer = ChargerReviewSerializer(data=self.get_queryset(),
                                             many=True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data)

    def create(self, request):
        serializer = ChargerReviewSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return ChargerReview.objects.all()

    @list_route(methods=['POST'])
    def create_review(self, request):
        statId = request.data.get("statId", None)
        user = request.user
        title = request.data.get("title", None)
        star = request.data.get("star", None)
        charger = Charger.objects.filter(statId=statId)[0]
        chargerReview = ChargerReview.objects.create(
                charger=charger, title=title,
                star=star, user=user)
        serializer = ChargerReviewSerializer(chargerReview)
        return Response(serializer.data)
