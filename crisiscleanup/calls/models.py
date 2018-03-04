from django.db import models
from django.core.validators import RegexValidator
from .utils import ChoiceEnum
import uuid


class Language(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    class Meta:
        db_table = 'language'
    
    def __str__(self):
        return str(self.name)

class Gateway(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    external_gateway_id = models.CharField(max_length=25, unique=True, null=True)
    name = models.CharField(max_length=100, null=True)
    agent_username = models.CharField(max_length=100, null=True)
    agent_password = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)
    language = models.ForeignKey('Language')

    class Meta:
        db_table = 'gateway'

    def __str__(self):
        return str(self.name)

class User(models.Model):
    # validators
    phone_regex = RegexValidator(
        regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    # fields
    # Id comes from a seperate API, so overriding the default here
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
    last_used_gateway = models.ForeignKey(
        'Gateway', on_delete=models.SET_NULL, null=True)
    last_used_state = models.CharField(max_length=50, blank=True, null=True)
    # A list of all articles which the user has read
    read_articles = models.ManyToManyField('Article', blank=True)
    # A list of all training the user has completed
    training_completed = models.ManyToManyField('TrainingModule', blank=True)
    # A quick reference name, master name is stored in user API
    name = models.CharField(max_length=100, null=True)
    #  A comma delimited list of the languages which they support calls for
    languages = models.ManyToManyField('Language')

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
        return str(self.title)


class TrainingModule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    video_url = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = 'training_module'

    def __str__(self):
        return str(self.title)


class TrainingQuestion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    module = models.ForeignKey('TrainingModule')
    question = models.CharField(max_length=500)
    answer = models.BooleanField()
    class Meta:
        db_table = 'training_question'

    def __str__(self):
        return str(self.question)

class CallType(ChoiceEnum):
    UNKNOWN = 'Unknown'
    INBOUND_MISSED = 'Inbound Missed'
    INBOUND_ANSWERED = 'Inbound Answered'
    OUTBOUND = 'Outbound'

class Call(models.Model):
    call_start = models.DateTimeField()
    duration = models.PositiveIntegerField()
    # The person calling in to CC or who we are calling
    caller = models.ForeignKey('Caller')
    gateway = models.ForeignKey('Gateway')
    # The number of the CC volunteer
    user_number = models.CharField(max_length=255, null=True, blank=True)
    # The (probably toll-free) CC number
    ccu_number = models.CharField(max_length=255, null=True, blank=True)
    # Connect First ID (uii)
    external_id = models.CharField(max_length=30)
    call_type = models.CharField(max_length=30, choices=CallType.choices(), default=CallType.UNKNOWN)
    # Call disposition/status from translations.json file
    call_result = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    language = models.ForeignKey('Language')

    class Meta:
        db_table = 'call'

    def __str__(self):
        return 'Call to/from {} at {}'.format(caller.phone_number, call_start)

class CallWorksite(models.Model):
    """Records which worksite(s) a call was about
    """
    call = models.ForeignKey('Call', on_delete=models.CASCADE)
    worksite = models.UUIDField()

    class Meta:
        db_table = 'call_worksite'

    def __str__(self):
        return str(self.name)

class Caller(models.Model):
    # validators
    phone_regex = RegexValidator(
        regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    # fields
    # Id comes from a separate API
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    region = models.CharField(max_length=255, null=True)
    preferred_language = models.ForeignKey('Language')

    class Meta:
        db_table = 'caller'

    def __str__(self):
        return str(self.name)

class CallerWorksite(models.Model):
    """Records to which worksite(s) a caller is associated
    """
    caller = models.ForeignKey('Caller', on_delete=models.CASCADE)
    worksite = models.UUIDField()

    class Meta:
        db_table = 'caller_worksite'

    def __str__(self):
        return str(self.name)

class ConnectFirstCallResult(ChoiceEnum):
    UNKNOWN = 'Unknown'
    CONNECTED = 'Connected'
    ABANDON = 'Abandoned'
    DEFLECTED = 'Deflected'

class ConnectFirstEvent(models.Model):
    uii = models.CharField(max_length=30) # CF manual specifies these are 30 chars
    call_start = models.DateTimeField()
    enqueue_time = models.DateTimeField()
    dequeue_time = models.DateTimeField()
    queue_duration = models.CharField(max_length=30)
    ani = models.CharField(max_length=30)
    dnis = models.CharField(max_length=30)
    outbound_disposition = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()
    gate_id = models.CharField(max_length=30)
    gate_name = models.CharField(max_length=30)
    recording_url = models.CharField(max_length=500)
    agent_id = models.CharField(max_length=30)
    agent_username = models.CharField(max_length=30)
    agent_phone = models.CharField(max_length=300)
    agent_disposition = models.CharField(max_length=30)
    sess_duration = models.PositiveIntegerField()
    agent_externid = models.CharField(max_length=50)
    agent_notes = models.TextField()
    call_result = models.CharField(max_length=100, choices=ConnectFirstCallResult.choices(), default=ConnectFirstCallResult.UNKNOWN)
    class Meta:
        db_table = 'connectfirst_event'

    def __str__(self):
        return str(self.id)

