from rest_framework.viewsets import ModelViewSet
from appointments.models import Appointment
from .serializers import AppointmentSerializer
import sentry_sdk

class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        try:
            professional_id = self.request.query_params.get("professional")
            if professional_id:
                return self.queryset.filter(professional_id=professional_id)
            return self.queryset
        except Exception as e:
            sentry_sdk.capture_exception(e)
            raise