from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from .models import User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'year', 'sex', 'place', 'profile', 'password', 'car_type')
        extra_kwargs = {'password': {'write_only': True},
                        'profile' : {'required':False}
                        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
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
        fields = ('pk', 'username', 'email', 'year', 'sex', 'place', 'profile', 'car_type')
        extra_kwargs = {'username': {'required': False},
                        'email': {'required': False},
                        'year': {'required': False},
                        'sex': {'required': False},
                        'place': {'required': False},
                        'profile': {'required': False},
                        'car_type': {'car_type':False},
                        }

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.year = validated_data.get("year", instance.year)
        instance.sex = validated_data.get("sex", instance.sex)
        instance.place = validated_data.get("place", instance.place)
        instance.profile = validated_data.get("profile", instance.profile)
        instance.car_type = validated_data.get("car_type", instance.car_type)
        instance.save()
        return instance

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)

            if user:
                # From Django 1.10 onwards the `authenticate` call simply
                # returns `None` for is_active=False users.
                # (Assuming the default `ModelBackend` authentication backend.)
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
