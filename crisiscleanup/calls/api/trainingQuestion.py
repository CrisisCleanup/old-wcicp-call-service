from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from crisiscleanup.calls.api.serializers.trainingQuestion import TrainingQuestionSerializer
from crisiscleanup.calls.models import TrainingQuestion
from crisiscleanup.taskapp.celery import debug_task


class TrainingQuestionViewSet(viewsets.ModelViewSet):
    queryset = TrainingQuestion.objects.all()
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ()
    filter_fields = ()
    serializer_class = TrainingQuestionSerializer

    @list_route()
    def test_celery(self, request):
        resp = {
            'task_id': debug_task.delay().id
        }
        return Response(resp, status=status.HTTP_200_OK)
