from rest_framework import serializers
from .models import Caveat, CaveatManager

class UserForCaveatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Caveat
        fields = ('pk','title')


class UserFromCaveatManagerSerializer(serializers.ModelSerializer):
    caveat = UserForCaveatSerializer(read_only=True)

    class Meta:
        model = CaveatManager
        fields = ('pk', 'caveat', 'count')
