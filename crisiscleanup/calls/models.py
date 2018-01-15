from django.db import models
from django.core.validators import RegexValidator
import uuid


class User(models.Model):
    # validators
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    # fields
    # Id comes from a seperate API
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    willing_to_receive_calls = models.BooleanField(default=False)
    # Hero helps the other volunteers who take calls
    willing_to_be_call_hero = models.BooleanField(default=False)
    # Hero helps people fix map pins
    willing_to_be_pin_hero = models.BooleanField(default=False)
    last_used_phone_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True)
    last_used_gateway = models.ForeignKey(
        'Gateway', on_delete=models.SET_NULL, null=True)
    last_used_state = models.CharField(max_length=50, null=True)
    # Whether or not the user's training is current
    is_trained = models.BooleanField(default=False)
    # Whether or not the user has been notified of any updates
    is_up_to_date = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return str(self.name)


class Gateway(models.Model):
    class Meta:
        db_table = 'gateway'

    def __str__(self):
        return str(self.name)


class Call(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    number = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'call'

    def __str__(self):
        return str(self.name)
