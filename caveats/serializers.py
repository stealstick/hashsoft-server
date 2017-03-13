from rest_framework import serializers

from accounts.models import User
from .models import Caveat, CaveatManager

class UserForOtherSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)


class UserForCaveatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Caveat
        fields = ('pk','title')


class UserFromCaveatManagerSerializer(serializers.ModelSerializer):
    caveat = UserForCaveatSerializer(read_only=True)

    class Meta:
        model = CaveatManager
        fields = ('pk', 'caveat', 'count')


class CaveatSerializer(serializers.ModelSerializer):
    users = UserForOtherSerializer(read_only=True, many=True)

    class Meta:
        model = Caveat
        fields = ('pk', 'users', 'title')
