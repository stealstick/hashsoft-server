from rest_framework import serializers

from chargers.serializers import ReviewChargerSerializer
from accounts.models import User
from .models import ChargerReview, Charger

class UserForChargerReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'year', 'sex', 'place',
                  'profile', 'car_type', 'user_card')

class ChargerReviewSerializer(serializers.ModelSerializer):
    charger = ReviewChargerSerializer(many=False)
    user = UserForChargerReviewSerializer(many=False, read_only=True)

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
