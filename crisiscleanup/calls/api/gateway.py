from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from crisiscleanup.calls.api.serializers.gateway import GatewaySerializer
from crisiscleanup.calls.models import Gateway
from crisiscleanup.taskapp.celery import debug_task


class GatewayViewSet(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
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
        gateway = self.get_object()
        serializedData = self.get_serializer(gateway).data;
        #Calculate whether or not the user's training and read articles are up-to-date
        return Response(serializedData)

    def update(self, request, pk=None):
        gateway = self.get_object()
        serializer = GatewaySerializer(gateway, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        gateway = self.get_object()
        gateway.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)