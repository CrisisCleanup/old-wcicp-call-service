from rest_framework import serializers

from crisiscleanup.calls.models import User

class UserSerializer(serializers.ModelSerializer):
    read_articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    training_completed = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'willing_to_receive_calls', 'willing_to_be_call_hero',
                  'willing_to_be_pin_hero', 'last_used_phone_number', 'last_used_state',
                  'read_articles', 'training_completed', 'first_name', 'last_name')
