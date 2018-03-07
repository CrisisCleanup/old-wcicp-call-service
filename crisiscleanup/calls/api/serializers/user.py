from rest_framework import serializers
from pprint import pprint

from crisiscleanup.calls.models import User, Language

class UserSerializer(serializers.ModelSerializer):
    read_articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    training_completed = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    languages = serializers.PrimaryKeyRelatedField(many=True, queryset=Language.objects.all())

    class Meta:
        model = User
        fields = ('id', 'willing_to_receive_calls', 'willing_to_be_call_hero', 'willing_to_be_call_center_support',
                  'willing_to_be_pin_hero', 'last_used_phone_number', 'last_used_state', 'last_used_gateway',
                  'read_articles', 'training_completed', 'name', 'languages')
        depth = 1
