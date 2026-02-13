from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Professional
from .serializers import ProfessionalSerializer
from appointments.models import Appointment
import sentry_sdk

class ProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['profession']
    search_fields = ['social_name', 'address', 'profession']

    def destroy(self, request, *args, **kwargs):
        try:
            professional = self.get_object()
            if Appointment.objects.filter(professional=professional).exists():
                return Response(
                    {"error": "Não é possível excluir um profissional com agendamentos associados."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            sentry_sdk.capture_exception(e)
            raise

    def get_queryset(self):
        try:
            return super().get_queryset()
        except Exception as e:
            sentry_sdk.capture_exception(e)
            raise