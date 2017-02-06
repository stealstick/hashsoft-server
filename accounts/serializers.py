from rest_framework import serializers
from .models import User, UserCarType

class UserCarTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCarType
        fields = ('pk','user', 'car')


class UserSerializer(serializers.ModelSerializer):
    usercartype_set = UserCarTypeSerializer(many=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'year', 'sex', 'place', 'profile', 'password', 'usercartype_set')
        extra_kwargs = {'password': {'write_only': True},
                        'profile' : {'required':False}
                        }

    def create(self, validated_data):
        userCarTypes_data = validated_data.pop('usercartype_set')
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        for userCarType_data in userCarTypes_data:
            UserCarType.objects.create(user=user, **userCarType_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.place = validated_data.get('place', instance.place)
        instance.year = validated_data.get('year', instance.year)
        instance.profile = validated_data.get('profile', instance.profile)
        return instance


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=30)

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance