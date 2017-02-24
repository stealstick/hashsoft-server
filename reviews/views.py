from rest_framework import viewsets
from .serializers import ChargerReviewSerializer
from .models import ChargerReview


class ChargerReviewViewSet(viewsets.ModelViewSet):
        serializer_class = ChargerReviewSerializer
        queryset = ChargerReview.objects.all()

        def perform_create(self, serializer):
                serializer.save(user=self.request.user)
