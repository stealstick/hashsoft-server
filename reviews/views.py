from rest_framework import viewsets
from .serializers import ChargerReviewSerializer
from .models import ChargerReview
from chargers.models import Charger
from rest_framework.response import Response


class ChargerReviewViewSet(viewsets.ModelViewSet):
        serializer_class = ChargerReviewSerializer

        def list(self, request, *args, **kwargs):
                statId = request.query_params.get("statId")
                if statId is not None:
                        try:
                                charger = Charger.objects.get(statId=statId)
                        except Charger.DoesNotExist:
                                return Response("DoesNotExist statId")
                        serializer = ChargerReviewSerializer(data=charger.review.all(), many=True)
                        serializer.is_valid(raise_exception=False)
                        return Response(serializer.data)

                serializer = ChargerReviewSerializer(data=self.get_queryset(), many=True)
                serializer.is_valid(raise_exception=False)
                return Response(serializer.data)

        def perform_create(self, serializer):
                serializer.save(user=self.request.user)

        def get_queryset(self):
                return ChargerReview.objects.all()
