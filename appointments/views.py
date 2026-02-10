from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(ModelViewSet):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        
        professional_id = self.request.query_params.get("professional")

        if professional_id:
            return self.queryset.filter(professional_id=professional_id)
        
        return self.queryset
