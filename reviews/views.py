from rest_framework import viewsets
from .models import ChargerReview
from .serializers import ChargerReviewSerializer


class ChargerReviewViewSet(viewsets.ModelViewSet):
        serializer_class = ChargerReviewSerializer
        queryset = ChargerReview.objects.all()
