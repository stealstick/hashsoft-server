from rest_framework import serializers

from chargers.serializers import ReviewChargerSerializer
from .models import ChargerReview, Charger


class ChargerReviewSerializer(serializers.ModelSerializer):
    charger = ReviewChargerSerializer(many=False)

    class Meta:
        model = ChargerReview
        fields = ('id', 'charger', 'user', 'title', 'text', 'star')
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def create(self, validated_data):
        validated_data_charger = validated_data.pop("charger")
        statId = validated_data_charger.get("statId", None)
        charger = Charger.objects.filter(statId=statId)[0]
        chargerReview = ChargerReview.objects.create(charger=charger,
                                                     **validated_data)
        return chargerReview
