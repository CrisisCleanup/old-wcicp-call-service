from django.db import models
from django.core.validators import RegexValidator
import uuid


class Gateway(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agent_id = models.IntegerField(null=True)
    gate_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    agent_username = models.CharField(max_length=100, null=True)
    agent_password = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'gateway'

    def __str__(self):
        return str(self.name)

class User(models.Model):
    # validators
    phone_regex = RegexValidator(
        regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    # fields
    # Id comes from a seperate API
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    # Willing to receive calls related to disasters associated to their organization
    willing_to_receive_calls = models.BooleanField(default=False)
    # Hero helps with all calls outside of organization disasters
    willing_to_be_call_hero = models.BooleanField(default=False)
    # Willing to support other call center operatives
    willing_to_be_call_center_support = models.BooleanField(default=False)
    # Hero helps people fix map pins
    willing_to_be_pin_hero = models.BooleanField(default=False)
    last_used_phone_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True)
    gateway = models.ForeignKey(
        'Gateway', on_delete=models.SET_NULL, null=True)
    last_used_state = models.CharField(max_length=50, null=True)
    # A list of all articles which the user has read
    read_articles = models.ManyToManyField('Article', blank=True)
    # A list of all training the user has completed
    training_completed = models.ManyToManyField('TrainingModule', blank=True)
    # A quick reference name, master name is stored in user API
    name = models.CharField(max_length=100, null=True)
    #  A comma delimited list of the languages which they support calls for
    supported_languages = models.CharField(max_length=254, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return str(self.name)


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    #TODO: Eventually will have types: Organization, Disaster, for now assume all global
    class Meta:
        db_table = 'article'

    def __str__(self):
        return str(self.name)


class TrainingModule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    video_url = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = 'training_module'

    def __str__(self):
        return str(self.name)


class TrainingQuestion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    module = models.ForeignKey('TrainingModule')
    question = models.CharField(max_length=500)
    answer = models.BooleanField()
    class Meta:
        db_table = 'training_question'

    def __str__(self):
        return str(self.name)


class Call(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    caller_number = models.CharField(max_length=255, null=True, blank=True)
    user_number = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank = True)

    class Meta:
        db_table = 'call'

    def __str__(self):
        return str(self.name)

class Caller(models.Model):
    # validators
    phone_regex = RegexValidator(
        regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    # fields
    # Id comes from a separate API
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    region = models.CharField(max_length=255, null=True)
    # Address break down
    address_street = models.CharField(max_length=255, null=True)
    address_city = models.CharField(max_length=255, null=True)
    address_state = models.CharField(max_length=50, null=True)
    address_unit = models.CharField(max_length=255, null=True)
    address_zipcode = models.CharField(max_length=14, null=True)
    # A list of all calls which the caller has made
    calls = models.ManyToManyField('Call', blank=True)
    name = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'caller'

    def __str__(self):
        return str(self.name)
