from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'year', 'sex', 'place', 'profile', 'password')
        extra_kwargs = {'password': {'write_only': True},
                        'profile' : {'required':False}
                        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        return user


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=30)

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'year', 'sex', 'place', 'profile')
        extra_kwargs = {'username': {'required': False},
                        'email': {'required': False},
                        'year': {'required': False},
                        'sex': {'required': False},
                        'place': {'required': False},
                        'profile': {'required': False},
                        }

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.year = validated_data.get("year", instance.year)
        instance.sex = validated_data.get("sex", instance.sex)
        instance.place = validated_data.get("place", instance.place)
        instance.profile = validated_data.get("username", instance.profile)
        instance.save()
        return instance