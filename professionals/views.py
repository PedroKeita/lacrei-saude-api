from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .models import Professional
from .serializers import ProfessionalSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['profession']

    search_fields = ['social_name', 'address', 'profession']



