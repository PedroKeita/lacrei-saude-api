from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from professionals.models import Professional
from appointments.models import Appointment
from django.utils import timezone
from datetime import timedelta

class AppointmentTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="123456")

        response = self.client.post("/api/token/", {
            "username": "admin",
            "password": "123456"
            })
        
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.professional = Professional.objects.create(
            social_name= "Doutor Teste",
            profession= "Cardiologista",
            address= "Rua Teste, 123",
            contact="99999999999"
        )

        self.appointment = Appointment.objects.create(
            professional=self.professional,
            date=timezone.now() + timedelta(days=1),
            customer_name="Cliente 1",
            status="CONFIRMED"
        )


    # TESTS CREATE APPOINTMENTS

    def test_create_appointment(self):
        url = "/api/appointments/"
        data = {
            "professional": self.professional.id,
            "date": (timezone.now() + timedelta(days=2)).isoformat(),
            "customer_name": "Cliente Novo",
            "status": "CONFIRMED"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appointment.objects.count(), 2)

    
    def test_create_appointment_in_past(self):
        url = "/api/appointments/"
        data = {
            "professional": self.professional.id,
            "date": (timezone.now() - timedelta(days=1)).isoformat(),
            "customer_name": "Cliente",
            "status": "CONFIRMED"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_appointment_missing_fields(self):
        url = "/api/appointments/"
        data = {
            "customer_name": "Cliente"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  


    def test_create_appointment_invalid_professional(self):
        url = "/api/appointments/"
        data = {
            "professional": 999,
            "date": (timezone.now() + timedelta(days=2)).isoformat(),
            "customer_name": "Cliente",
            "status": "CONFIRMED"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    # TESTS READ APPOINTMENTS

    def test_list_appointments(self):
        response = self.client.get("/api/appointments/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def  test_get_appointment_detail(self):
        url = f"/api/appointments/{self.appointment.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_appointment_not_found(self):
        response = self.client.get("/api/appointments/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    # TESTS UPDATE APPOINTMENTS

    def test_update_appointment(self):
        url = f"/api/appointments/{self.appointment.id}/"
        data = {
            "professional": self.professional.id,
            "date": (timezone.now() + timedelta(days=3)).isoformat(),
            "customer_name": "Cliente Atualizado",
            "status": "CONFIRMED"
         }

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.customer_name, "Cliente Atualizado")
        self.assertEqual(self.appointment.status, "CONFIRMED")


    # TESTS DELETE APPOINTMENTS

    def test_delete_appointment(self):
        url = f"/api/appointments/{self.appointment.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Appointment.objects.filter(id=self.appointment.id).exists())


    # TESTS BUSINESS RULES

    def test_cannot_create_two_appointments_same_time_same_professional(self):
        url = "/api/appointments/"
        date = self.appointment.date.isoformat()

        data = {
            "professional": self.professional.id,
            "date": date,
            "customer_name": "Cliente 2",
            "status": "CONFIRMED"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    # TESTS PERMISSIONS

    def test_cannot_acess_without_token(self):
        self.client.credentials()  

        response = self.client.get("/api/appointments/")  
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  