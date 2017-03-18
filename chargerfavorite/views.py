from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from chargers.models import Charger
from .models import ChargerFavorite
from .serializers import ChargerFavoriteSerializer


class ChargerFavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = ChargerFavoriteSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        post = request.POST.copy()
        post["user"] = request.user.pk
        serializer = ChargerFavoriteSerializer(data=post)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        chargerFavorite = ChargerFavorite.objects.get(pk=pk)
        chargerFavorite.delete()
        return Response()

    def get_queryset(self):
        return ChargerFavorite.objects.all()
