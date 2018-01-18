from rest_framework import serializers

from crisiscleanup.calls.models import Call


class CallSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    caller_number = serializers.CharField()
    user_number = serializers.CharField()

    class Meta:
        model = Call
        fields = ('id', 'caller_number', 'user_number')
