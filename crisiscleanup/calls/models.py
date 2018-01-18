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
    # A list of all articles which the user has read
    read_articles = models.ManyToManyField('Article', blank=True)
    # A list of all training the user has completed
    training_completed = models.ManyToManyField('TrainingModule', blank=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    
    class Meta:
        db_table = 'user'

    def __str__(self):
        return str(self.name)


class Gateway(models.Model):
    class Meta:
        db_table = 'gateway'

    def __str__(self):
        return str(self.name)


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    #TODO: Eventually will have types: Organization, Disaster, for now assume all global
    class Meta:
        db_table = 'article'

    def __str__(self):
        return str(self.name)


class TrainingModule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True)
    video_path = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = 'training_module'

    def __str__(self):
        return str(self.name)


class TrainingQuestion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    module = models.ForeignKey('TrainingModule')
    question = models.CharField(max_length=100)
    answer = models.BooleanField()
    class Meta:
        db_table = 'training_question'

    def __str__(self):
        return str(self.name)


class Call(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    caller_number = models.CharField(max_length=255, null=True, blank=True)
    user_number = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'call'

    def __str__(self):
        return str(self.name)

class Caller(models.Model):
    # validators
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    # fields
    # Id comes from a seperate API
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    phone_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True)
    location = models.CharField(max_length=255, null=True)
    # A list of all calls which the caller has made
    calls = models.ManyToManyField('Call', blank=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    
    class Meta:
        db_table = 'caller'

    def __str__(self):
        return str(self.name)