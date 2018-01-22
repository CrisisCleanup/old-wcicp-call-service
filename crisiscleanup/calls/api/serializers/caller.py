from rest_framework import serializers

from crisiscleanup.calls.models import Caller

class CallerSerializer(serializers.ModelSerializer):
    calls = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Caller
        fields = ('id', 'phone_number', 'region', 'address_street', 'address_city', 'address_state', 'address_unit', 'address_zipcode' ,'calls', 'first_name', 'last_name')
