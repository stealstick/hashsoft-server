from rest_framework import serializers
from chargers.models import Charger

class chargerField(serializers.RelatedField):
    queryset = Charger.objects.all()

    def to_internal_value(self, data):
        obj = Charger.objects.get(statId=data)
        if obj is None:
            raise serializers.ValidationError(
                'id is a required field.'
            )
        return obj

    def to_representation(self, value):
        return value.statId