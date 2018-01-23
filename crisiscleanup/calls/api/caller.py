from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from crisiscleanup.calls.api.serializers.caller import CallerSerializer
from crisiscleanup.calls.models import Caller
from crisiscleanup.calls.models import Call
from crisiscleanup.taskapp.celery import debug_task


class CallerViewSet(viewsets.ModelViewSet):
    queryset = Caller.objects.all()
    serializer_class = CallerSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ()
    filter_fields = ()

    @list_route()
    def test_celery(self, request):
        resp = {
            'task_id': debug_task.delay().id
        }
        return Response(resp, status=status.HTTP_200_OK)


    @detail_route(methods=['get'])
    def get_detail(self, request, pk=None):
        caller = self.get_object()
        serializedData = self.get_serializer(caller).data;
        #Calculate 
        return Response(serializedData)
    
    