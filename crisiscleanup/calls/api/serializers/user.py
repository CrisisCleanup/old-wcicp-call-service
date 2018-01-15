from rest_framework import serializers

from crisiscleanup.calls.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'willing_to_receive_calls', 'willing_to_be_call_hero',
                  'willing_to_be_pin_hero', 'last_used_phone_number', 'last_used_gateway', 'last_used_state', 'read_articles', 'training_completed')
