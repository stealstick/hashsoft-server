from rest_framework import serializers
from .models import ChargerReview

class ChargerReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChargerReview
        fields = '__all__'