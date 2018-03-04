from rest_framework import serializers

from crisiscleanup.calls.models import Caller

class CallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caller
        fields = ('id', 'name', 'phone_number', 'region', 'preferred_language')
        depth = 1
