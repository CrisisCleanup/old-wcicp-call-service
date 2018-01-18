from rest_framework import serializers

from crisiscleanup.calls.models import Gateway


class GatewaySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    title= serializers.CharField()

    class Meta:
        model = Gateway
        fields = ('id', 'title')
