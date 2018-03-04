from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from crisiscleanup.calls.api.serializers.language import LanguageSerializer
from crisiscleanup.calls.models import Language
from crisiscleanup.taskapp.celery import debug_task


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    
    