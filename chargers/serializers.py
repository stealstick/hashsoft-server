from rest_framework import serializers

from .models import Charger


class ChargerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charger
        fields = '__all__'

class ChargerSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charger
        fields = ('statId', 'stat')
class ChargerSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charger
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
        }


class ReviewChargerSerializer(serializers.Serializer):
    statId = serializers.CharField(max_length=100)
