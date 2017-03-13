from rest_framework import serializers

from accounts.models import User,UserCard


class UserForOtherSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)


class UserCardSerializer(serializers.ModelSerializer):
    user = UserForOtherSerializer(read_only=True)

    class Meta:
        model = UserCard
        fields = ('pk', 'serial_number', 'balance', 'user')


class UserCardUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCard
        fields = ('pk', 'serial_number', 'balance')
        extra_kwargs = {'serial_number': {'read_only': True}
                        }

    def update(self, instance, validated_data):
        instance.balance = validated_data.get("balance", instance.balance)
        instance.save()
        return instance
