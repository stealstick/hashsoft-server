from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ChargerReviewSerializer
from chargers.models import Charger
from .models import ChargerReview
from rest_framework import status


class ChargerReviewViewSet(viewsets.ModelViewSet):
        serializer_class = ChargerReviewSerializer
        queryset = ChargerReview.objects.all()
