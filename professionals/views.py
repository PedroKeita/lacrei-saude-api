from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .models import Professional
from .serializers import ProfessionalSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['profession']

    search_fields = ['social_name', 'address', 'profession']



