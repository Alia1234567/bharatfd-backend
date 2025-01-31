from django.test import TestCase
from backend.models import User

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username='testuser', email='testuser@example.com', password='password123')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
