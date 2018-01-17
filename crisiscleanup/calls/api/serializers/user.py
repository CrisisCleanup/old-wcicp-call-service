from rest_framework import serializers

from crisiscleanup.calls.models import User
from crisiscleanup.calls.api.serializers.article import ArticleSerializer
from crisiscleanup.calls.api.serializers.trainingModule import TrainingModuleSerializer


class UserSerializer(serializers.ModelSerializer):
    read_articles = ArticleSerializer(many=True)
    training_completed = TrainingModuleSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'willing_to_receive_calls', 'willing_to_be_call_hero',
                  'willing_to_be_pin_hero', 'last_used_phone_number', 'last_used_gateway', 'last_used_state',
                  'read_articles', 'training_completed', 'first_name', 'last_name')
