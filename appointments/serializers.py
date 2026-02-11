from rest_framework import serializers
from .models import Appointment
from django.utils import timezone

class AppointmentSerializer(serializers.ModelSerializer):
    class meta:
        model = Appointment
        fields = "__all__"

    def validate_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Não é possivel agendar para uma data passada")
        return value    
    
    def validate(self, data):
        professional = data.get('professional')
        data = data.get('date')

        existing_appointment = Appointment.objects.filter(
            professional=professional,
            date=date
        ).exclude(pk=self.instance.pk if self.instance else None)

        if existing_appointment.exists():
            raise serializers.ValidationError(
                {"date": "Este profissional já possui um agendamento neste horário indicado."}
            )   

        return data 



