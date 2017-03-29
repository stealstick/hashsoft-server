from rest_framework import serializers

from .models import Board, Dataroom


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'

class DataroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dataroom
        fields = '__all__'
