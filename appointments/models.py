from django.db import models
from professionals.models import Professional
from django.utils import timezone

class Appointment(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pendente'),
        ('CONFIRMED', 'Confirmado'),
        ('CANCELED', 'Cancelado'),
        ('COMPLETED', 'Concluído')
    ]
    date = models.DateTimeField()
    professional = models.ForeignKey(Professional, on_delete=models.PROTECT, related_name = "appointments")

    customer_name = models.CharField(max_length=150, help_text="Nome do cliente", default="Cliente")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.customer_name} - {self.professional.social_name} ({self.date})"