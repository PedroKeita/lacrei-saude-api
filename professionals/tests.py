from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from professionals.models import Professional
from appointments.models import Appointment
from django.utils import timezone
from datetime import timedelta



class ProfessionalDeleteTests(APITestCase):
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

        
      


    # TESTS CREATE PROFESSIONALS

    def test_create_professional(self):
        url = "/api/professionals/"
        data = {
            "social_name": "Doutor Teste",
            "profession": "Cardiologista",
            "address": "Rua Teste, 123",
            "contact": "99999999999"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Professional.objects.count(), 2)


    def test_create_professional_missing_fields(self):
        url = "/api/professionals/"
        data = {
            "social_name": "Doutor Teste",
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    

    # READ TESTS

    def test_list_professionals(self):
        response = self.client.get("/api/professionals/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_professional_detail(self):
        url = f"/api/professionals/{self.professional.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    

    def test_get_professional_not_found(self):
        response = self.client.get("/api/professionals/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)   



    # TESTS UPDATE PROFESSIONALS

    def test_update_professional(self):
        url = f"/api/professionals/{self.professional.id}/"
        data = {
            "social_name": "Dr Teste atualizado",
            "profession": "Neurologista",
            "address": "Rua B",
            "contact": "11777777777"
        }

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.professional.refresh_from_db()
        self.assertEqual(self.professional.social_name, "Dr Teste atualizado")


    # TESTS DELETE PROFESSIONALS

    def test_delete_professional_without_appointments(self):
        url = f"/api/professionals/{self.professional.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Professional.objects.filter(id=self.professional.id).exists())

    
    def test_cannot_delete_professional_with_appointments(self):
        Appointment.objects.create(
            professional=self.professional,
            date=timezone.now() + timedelta(days=1),
            customer_name="Cliente",
            status="CONFIRMED"
        )

        url = f"/api/professionals/{self.professional.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(Professional.objects.filter(id=self.professional.id).exists())



    # TESTS PERMISSIONS

    def test_cannot_acess_without_token(self):
        self.client.credentials() 
        response = self.client.get("/api/professionals/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

