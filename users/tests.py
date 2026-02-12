from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class UserAuthTests(APITestCase):
    def setUp(self):
        self.register_url = "/api/users/register/"
        self.login_url = "/api/token/"
        self.user_data = {
            "username": "teste123",
            "password": "password123",
            "email": "teste@teste.com"
        }

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="teste123").exists())   

    def test_login_and_get_token(self):
        User.objects.create_user(**self.user_data)
        response = self.client.post(self.login_url, {
            "username": "teste123",
            "password": "password123"
        })     
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
