from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('id', 'user', 'title', 'content', 'piture')
        extra_kwargs = {'user': {'required': False},
                        }
