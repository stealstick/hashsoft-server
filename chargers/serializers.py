from rest_framework import serializers
from .models import Charger

class ChargerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charger
        fields = ('statId', 'statNm',  'chgerId', 'chgerType', 'stat', 'addrDoro', 'addrDoro','lat','lng','useTime','LastUsedTime')