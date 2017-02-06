from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'year', 'sex', 'place', 'profile', 'password')
        extra_kwargs = {'password': {'write_only': True},
                        'profile' : {'required':False}
                        }

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=30)