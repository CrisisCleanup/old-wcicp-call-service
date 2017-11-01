from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from crisiscleanup.calls.api.serializers.call import CallSerializer
from crisiscleanup.calls.models import Call
from crisiscleanup.taskapp.celery import debug_task


class CallViewSet(viewsets.ModelViewSet):
    queryset = Call.objects.all()
    serializer_class = CallSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('number',)
    filter_fields = ('number',)

    @list_route()
    def test_celery(self, request):
        resp = {
            'task_id': debug_task.delay().id
        }
        return Response(resp, status=status.HTTP_200_OK)
