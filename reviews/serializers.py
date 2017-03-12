from rest_framework import serializers

from chargers.serializers import ReviewChargerSerializer
from .models import ChargerReview, Charger


class ChargerReviewSerializer(serializers.ModelSerializer):
    charger = ReviewChargerSerializer()

    class Meta:
        model = ChargerReview
        fields = ('id','charger', 'user', 'title', 'text', 'star')
        extra_kwargs = {'user': {'required': False},
                        }

    def create(self, validated_data):
        validated_data_charger = validated_data.pop("charger")
        charger = Charger.objects.get(statId=validated_data_charger.get("statId", None))
        chargerReview = ChargerReview.objects.create(charger=charger,**validated_data)
        return chargerReview
