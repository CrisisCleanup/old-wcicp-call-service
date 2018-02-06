from rest_framework import serializers

from crisiscleanup.calls.models import TrainingQuestion
from crisiscleanup.calls.models import TrainingModule

class TrainingQuestionSerializer(serializers.ModelSerializer):
    module = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=TrainingModule.objects.all())
    class Meta:
        model = TrainingQuestion
        fields = ('id', 'question', 'answer', 'module')
