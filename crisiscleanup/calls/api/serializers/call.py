from rest_framework import serializers

from crisiscleanup.calls.models import Call


class CallSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    number = serializers.CharField()

    class Meta:
        model = Call
        fields = ('id', 'number')
