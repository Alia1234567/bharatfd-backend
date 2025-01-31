from rest_framework.test import APITestCase
from src.user.models import User
from rest_framework import status

class UserApiTestCase(APITestCase):
    def test_create_user(self):
        data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'password123'}
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
