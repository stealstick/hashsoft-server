from rest_framework import serializers

from .models import Warnin


class WarningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warnin
        fields = ('pk', 'users','title')


class UserForWarningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warnin
        fields = ('pk','title')
