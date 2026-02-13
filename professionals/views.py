from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .models import Professional
from .serializers import ProfessionalSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from appointments.models import Appointment
from rest_framework.response import Response
from rest_framework import status

class ProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['profession']

    search_fields = ['social_name', 'address', 'profession']

    def destroy(self, request, *args, **kwargs):
        professional = self.get_object()

        if Appointment.objects.filter(professional=professional).exists():
            return Response({"error": "Não é possível excluir um profissional com agendamentos associados."}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        return super().destroy(request, *args, **kwargs)


