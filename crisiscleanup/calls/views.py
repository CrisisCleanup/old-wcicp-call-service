from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core import serializers
from django.core.exceptions import PermissionDenied
from datetime import datetime
import pytz

from .models import ConnectFirstEvent

import json
import os
import base64


# Create your views here.

@csrf_exempt
@require_POST
def connect_first_inbound(request):
    username = os.environ.get('CONNECT_FIRST_USERNAME')
    password = os.environ.get('CONNECT_FIRST_PASSWORD')

    uname = None
    passwd = None
    if 'HTTP_AUTHORIZATION' in request.META:
        auth = request.META['HTTP_AUTHORIZATION'].split()
        if len(auth) == 2:
            if auth[0].lower() == "basic":
                uname, passwd = base64.b64decode(auth[1]).decode('ascii').split(':')

    if uname != username or passwd != password or uname == None or passwd == None:
        raise PermissionDenied

    min_date = '0001-01-01 00:00:00'
    date_format = '%Y-%m-%d %H:%M:%S'
    timezone = pytz.timezone('America/Chicago')
    call_start = request.POST.get('call_start', min_date)
    enqueue_time = request.POST.get('enqueue_time', min_date)
    dequeue_time = request.POST.get('dequeue_time', min_date)

    event = ConnectFirstEvent()

    event.uii = request.POST.get('uii', "")

    # TODO: Handle if these aren't in the right format
    event.call_start =  timezone.localize(datetime.strptime(call_start, date_format), is_dst=None)
    event.enqueue_time = timezone.localize(datetime.strptime(enqueue_time, date_format), is_dst=None)
    event.dequeue_time = timezone.localize(datetime.strptime(dequeue_time, date_format), is_dst=None)
    event.queue_duration = request.POST.get('queue_duration', 0) or 0
    event.ani = request.POST.get('ani', "")
    event.dnis = request.POST.get('dnis', "")
    event.outbound_disposition = request.POST.get('outbound_disposition', "")
    event.duration = request.POST.get('duration', 0) or 0
    event.gate_id = request.POST.get('gate_id', "")
    event.gate_name = request.POST.get('gate_name', "")
    event.recording_url = request.POST.get('recording_url', "")
    event.agent_id = request.POST.get('agent_id', "")
    event.agent_username = request.POST.get('agent_username', "")
    event.agent_phone = request.POST.get('agent_phone', "")
    event.agent_disposition = request.POST.get('agent_disposition', "")
    event.sess_duration = request.POST.get('sess_duration', 0) or 0
    event.agent_externid = request.POST.get('agent_externid', "")
    event.agent_notes = request.POST.get('agent_notes', "")
    event.call_result = request.POST.get('call_result', "")

    event.save()
    event.save_call()

    return HttpResponse(serializers.serialize("json", [event]))