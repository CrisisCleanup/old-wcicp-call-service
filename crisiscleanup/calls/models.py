from django.db import models
from django.core.validators import RegexValidator
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
    # ID in the Crisis Cleanup user service
    cc_id = models.IntegerField(null=False, blank=False)
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
        'Gateway', on_delete=models.SET_NULL, null=True, blank=True)
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
        indexes = [
            models.Index(fields=['cc_id'], name='IX_user_cc_id')
        ]

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

class Call(models.Model):
    INBOUND = 'INBOUND'
    UNKNOWN = 'UNKNOWN'
    INBOUND_MISSED = 'INBOUND_MISSED'
    INBOUND_ANSWERED = 'INBOUND_ANSWERED'
    OUTBOUND = 'OUTBOUND'
    CALL_TYPE_CHOICES = (
        (INBOUND, 'Inbound'),
        (UNKNOWN, 'Unknown'),
        (INBOUND_MISSED, 'Inbound Missed'),
        (INBOUND_ANSWERED, 'Inbound Answered'),
        (OUTBOUND, 'Outbound')
    )
    call_start = models.DateTimeField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    # The person calling in to CC or who we are calling
    caller = models.ForeignKey('Caller', null=True, blank=True)
    gateway = models.ForeignKey('Gateway')
    # The number of the CC volunteer
    user_number = models.CharField(max_length=255, null=True, blank=True)
    # The (probably toll-free) CC number
    ccu_number = models.CharField(max_length=255, null=True, blank=True)
    # Connect First ID (uii)
    external_id = models.CharField(max_length=30, unique=True)
    call_type = models.CharField(max_length=30, choices=CALL_TYPE_CHOICES, default=UNKNOWN)
    # Call disposition/status from translations.json file
    call_result = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    language = models.ForeignKey('Language', null=True, blank=True)

    class Meta:
        db_table = 'call'

    def __str__(self):
        return 'Call to/from {} at {}'.format(self.caller.phone_number, self.call_start)

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    # Unique by phone number
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, unique=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    preferred_language = models.ForeignKey('Language', null=True, blank=True)

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

class ConnectFirstEvent(models.Model):
    UNKNOWN = 'UNKNOWN'
    CONNECTED = 'CONNECTED'
    ABANDON = 'ABANDON'
    DEFLECTED = 'DEFLECTED'
    CALL_RESULT_CHOICES = (
        (UNKNOWN, 'Unknown'),
        (CONNECTED, 'Connected'),
        (ABANDON, 'Abandoned'),
        (DEFLECTED, 'Deflected')
    )

    uii = models.CharField(max_length=30) # CF manual specifies these are 30 chars
    call_start = models.DateTimeField(null=True, blank=True)
    enqueue_time = models.DateTimeField(null=True, blank=True)
    dequeue_time = models.DateTimeField(null=True, blank=True)
    queue_duration = models.PositiveIntegerField(null=True, blank=True)
    ani = models.CharField(max_length=30)
    dnis = models.CharField(max_length=30)
    outbound_disposition = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(null=True, blank=True)
    gate_id = models.CharField(max_length=30)
    gate_name = models.CharField(max_length=30)
    recording_url = models.CharField(max_length=500)
    agent_id = models.CharField(max_length=30)
    agent_username = models.CharField(max_length=30)
    agent_phone = models.CharField(max_length=300)
    agent_disposition = models.CharField(max_length=30)
    sess_duration = models.PositiveIntegerField(null=True, blank=True)
    agent_externid = models.CharField(max_length=50)
    agent_notes = models.TextField()
    call_result = models.CharField(max_length=100, choices=CALL_RESULT_CHOICES, default=UNKNOWN)
    class Meta:
        db_table = 'connectfirst_event'

    def __str__(self):
        return str(self.id)

    def save_call(self):
        call = Call.objects.filter(external_id=self.uii).first()
        if call is None:
            call = Call(external_id=self.uii)

        caller = Caller.objects.filter(phone_number=self.ani).first()
        if caller is None:
            caller = Caller.objects.create(phone_number=self.ani)

        gateway = Gateway.objects.filter(external_gateway_id=self.gate_id).first()
        if gateway is None:
            language = Language.objects.filter(code="en").first()
            gateway = Gateway.objects.create(external_gateway_id=self.gate_id, name=self.gate_name, language=language)

        call.call_start = self.call_start
        call.duration = self.duration
        call.caller = caller
        call.gateway = gateway
        call.ccu_number = self.dnis

        if (self.call_result == ConnectFirstEvent.ABANDON or self.call_result == ConnectFirstEvent.DEFLECTED):
            call.call_type = Call.INBOUND_MISSED
        else:
            call.call_type = Call.INBOUND_ANSWERED

        call.save()

