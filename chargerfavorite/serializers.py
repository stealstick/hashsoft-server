from rest_framework import serializers

from chargers.models import Charger
from .models import ChargerFavorite


class ChargerForChargerFavoirteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charger
        fields = '__all__'


class ChargerFavoirteForChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Charger
        fields = ('pk', 'statId')


class UserForChargerFavoriteSerializer(serializers.ModelSerializer):
    charger = ChargerForChargerFavoirteSerializer(many=False)

    class Meta:
        model = ChargerFavorite
        fields = ('pk', 'charger')


class ChargerFavoriteSerializer(serializers.ModelSerializer):
    charger = ChargerFavoirteForChargeSerializer(many=False)

    class Meta:
        model = ChargerFavorite
        fields = ('pk', 'user', 'charger')
        extra_kwargs = {
                        'user': {'required': False},
                        }

    def create(self, validated_data):
        charger = validated_data.get("charger")
        user = validated_data.get("user")
        chargerFavorite = ChargerFavorite.objects.create(user=user, charger=charger)
        return chargerFavorite

    def validate(self, attrs, **kwargs):
        charger = attrs.get("charger")
        statId = charger.get("statId")
        try:
            charger = Charger.objects.filter(statId=statId)[0]
        except:
            raise serializers.ValidationError(detail='statId doesn\'t exist')
        chargerFavorite = ChargerFavorite.objects.filter(user=attrs["user"], charger=charger)
        if chargerFavorite.count():
            raise serializers.ValidationError(detail='User aleady has this favorite charger')
        attrs["charger"] = charger
        return attrs
