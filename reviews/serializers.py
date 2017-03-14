from rest_framework import serializers

from chargers.serializers import ReviewChargerSerializer
from .models import ChargerReview, Charger


class ChargerReviewSerializer(serializers.ModelSerializer):
    charger = ReviewChargerSerializer(many=False)

    class Meta:
        model = ChargerReview
        fields = ('id', 'charger', 'user', 'title', 'text', 'star')
        extra_kwargs = {'user': {'required': False},
                        }

    def create(self, validated_data):
        validated_data_charger = validated_data.pop("charger")
        statId = validated_data_charger.get("statId", None)
        # TODO 충전기 모델이 각각 필요하지만 시간이 없어서 못바꿀 확률이 높아서 [0]으로 임시 수정
        charger = Charger.objects.filter(statId=statId)[0]
        chargerReview = ChargerReview.objects.create(charger=charger,
                                                     **validated_data)
        return chargerReview
