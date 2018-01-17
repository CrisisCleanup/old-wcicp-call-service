from rest_framework import serializers

from crisiscleanup.calls.models import Call


class CallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Call
        fields = ('id', 'caller_number', 'user_number')
