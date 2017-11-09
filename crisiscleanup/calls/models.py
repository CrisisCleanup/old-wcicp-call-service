from django.db import models
from django.core.validators import RegexValidator
import uuid


class User(models.Model):
    # validators
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    # fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    willing_to_receive_calls = models.BooleanField()
    # Hero helps the other volunteers who take calls
    willing_to_be_call_hero = models.BooleanField()
    # Hero helps people fix map pins
    willing_to_be_pin_hero = models.BooleanField()
    last_used_phone_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True)
    last_used_gateway = models.ForeignKey(
        'Gateway', on_delete=models.SET_NULL, null=True)
    last_used_state = models.CharField(max_length=50)

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'call'

    def __str__(self):
        return str(self.name)
