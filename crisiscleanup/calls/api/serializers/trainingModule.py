from rest_framework import serializers

from crisiscleanup.calls.models import TrainingModule


class TrainingModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingModule
        fields = ('id', 'title', 'description', 'video_url')
