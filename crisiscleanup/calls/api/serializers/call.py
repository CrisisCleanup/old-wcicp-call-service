from rest_framework import serializers

from crisiscleanup.calls.models import Call, Gateway, Caller


class CallSerializer(serializers.ModelSerializer):
    gateway = serializers.PrimaryKeyRelatedField(queryset=Gateway.objects)
    caller = serializers.PrimaryKeyRelatedField(queryset=Caller.objects)

    class Meta:
        model = Call
        fields = ('id', 'call_start', 'duration','caller', 'gateway', 'user_number', 'ccu_number', 'external_id',
                  'call_type', 'call_result', 'notes', 'language')
        depth = 1
