from rest_framework import serializers
from chargers.models import Charger

class chargerField(serializers.RelatedField):
    queryset = Charger.objects.all()

    def to_internal_value(self, data):
        try:
            obj = Charger.objects.get(statId=data)
        except Charger.DoesNotExist:
            raise serializers.ValidationError(
                'DoesNotExist statid'
            )
        return obj

    def to_representation(self, value):
        return value.statId