from rest_framework import serializers

from crisiscleanup.calls.models import TrainingQuestion


class TrainingQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingQuestion
        fields = ('id', 'question', 'answer')
