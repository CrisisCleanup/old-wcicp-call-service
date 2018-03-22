from rest_framework import serializers

from crisiscleanup.calls.models import Gateway
from crisiscleanup.calls.models import Language

class GatewaySerializer(serializers.ModelSerializer):
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects)

    class Meta:
        model = Gateway
        fields = ('id','external_gateway_id', 'name', 'agent_username', 'agent_password', 'active', 'language')
        depth = 1
