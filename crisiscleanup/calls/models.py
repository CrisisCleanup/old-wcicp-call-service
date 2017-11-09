from django.db import models
import uuid


class User(models.Model):
    # validators
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    # fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    willingToReceiveCalls = models.BooleanField()
    # Hero helps the other volunteers who take calls
    willingToBeCallHero = models.BooleanField()
    # Hero helps people fix map pins
    willingToBePinHero = models.BooleanField()
    lastUsedPhoneNumber = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    lastUsedGatewayId = models.ForeignKey('Gateway', on_delete=models.SET_NULL)
    lastUsedState = models.CharField(max_length=50)


    class Meta:
        db_table = 'calls'

    def __str__(self):
        return str(self.name)

class Call(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'calls'

    def __str__(self):
        return str(self.name)
