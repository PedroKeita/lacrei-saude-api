from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserTests(APITestCase):

    def setUp(self):
        self.register_url = "/api/users/register/"
        self.login_url = "/api/token/"
        self.refresh_url = "/api/token/refresh/"
        self.list_url = "/api/users/list/"

        self.user_data = {
            "username": "user1",
            "password": "password123",
            "email": "user1@test.com"
        }

        self.admin_data = {
            "username": "admin",
            "password": "admin123",
            "email": "admin@test.com"
        }

        self.admin_user = User.objects.create_superuser(**self.admin_data)

    
    # TESTS REGISTER

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="user1").exists())

    def test_register_missing_fields(self):
        response = self.client.post(self.register_url, {"username": "user2"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_duplicate_username(self):
        User.objects.create_user(**self.user_data)

        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

   
    # TESTS LOGIN AND TOKEN
    
    def test_login_and_get_token(self):
        User.objects.create_user(**self.user_data)

        response = self.client.post(self.login_url, {
            "username": "user1",
            "password": "password123"
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            "username": "x",
            "password": "y"
        })

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_refresh_token(self):
        User.objects.create_user(**self.user_data)

        login = self.client.post(self.login_url, {
            "username": "user1",
            "password": "password123"
        })

        refresh_token = login.data["refresh"]

        response = self.client.post(self.refresh_url, {
            "refresh": refresh_token
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

   
    # TESTS PERMISSIONS

    def test_admin_can_list_users(self):
        login = self.client.post(self.login_url, {
            "username": "admin",
            "password": "admin123"
        })

        token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_admin_cannot_list_users(self):
        User.objects.create_user(**self.user_data)

        login = self.client.post(self.login_url, {
            "username": "user1",
            "password": "password123"
        })

        token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cannot_access_list_without_token(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)