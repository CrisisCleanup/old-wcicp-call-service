from rest_framework import serializers

from crisiscleanup.calls.models import Gateway

class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ('id', 'name')
