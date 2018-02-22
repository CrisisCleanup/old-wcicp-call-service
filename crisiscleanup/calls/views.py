from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core import serializers
from django.core.exceptions import PermissionDenied

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

    if uname != username or passwd != password:
        raise PermissionDenied

    event = ConnectFirstEvent()

    event.uii = request.POST.get('uii', "")
    event.call_start = request.POST.get('call_start', "")
    event.enqueue_time = request.POST.get('enqueue_time', "")
    event.dequeue_time = request.POST.get('dequeue_time', "")
    event.queue_duration = request.POST.get('queue_duration', "")
    event.ani = request.POST.get('ani', "")
    event.dnis = request.POST.get('dnis', "")
    event.outbound_disposition = request.POST.get('outbound_disposition', "")
    event.duration = request.POST.get('duration', "")
    event.gate_id = request.POST.get('gate_id', "")
    event.gate_name = request.POST.get('gate_name', "")
    event.recording_url = request.POST.get('recording_url', "")
    event.agent_id = request.POST.get('agent_id', "")
    event.agent_username = request.POST.get('agent_username', "")
    event.agent_phone = request.POST.get('agent_phone', "")
    event.call_start = request.POST.get('call_start', "")
    event.agent_disposition = request.POST.get('agent_disposition', "")
    event.sess_duration = request.POST.get('sess_duration', "")
    event.agent_externid = request.POST.get('agent_externid', "")
    event.agent_notes = request.POST.get('agent_notes', "")

    event.save()


    return HttpResponse(serializers.serialize("json", [event]))