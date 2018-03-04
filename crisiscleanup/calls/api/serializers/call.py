from rest_framework import serializers

from crisiscleanup.calls.models import Call


class CallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Call
        fields = ('id', 'call_start', 'duration','caller', 'gateway', 'user_number', 'ccu_number', 'call_type', 'call_result', 'notes', 'language')
        depth = 1
