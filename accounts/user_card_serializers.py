from rest_framework import serializers

from accounts.models import UserCard


class UserCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCard
        fields = ('pk', 'serial_number', 'balance')


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
