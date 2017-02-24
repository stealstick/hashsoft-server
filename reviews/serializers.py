from rest_framework import serializers
from .models import ChargerReview
from chargers.rest_fields import chargerField


class ChargerReviewSerializer(serializers.ModelSerializer):
    charger = chargerField()

    class Meta:
        model = ChargerReview
        fields = '__all__'
        extra_kwargs = {'user': {'required': False},
                        }
