from rest_framework import serializers

from .models import Charger


class ChargerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charger
        fields = '__all__'


class ReviewChargerSerializer(serializers.Serializer):
    statId = serializers.CharField(max_length=100)
