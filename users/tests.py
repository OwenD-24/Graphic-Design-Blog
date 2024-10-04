from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UserRegistrationTests(TestCase):

    def setUp(self):
        self.url = reverse("register")
        self.user_data = {
            "username": "testuser",
            "password1": "SecurePassword123!",
            "password2": "SecurePassword123!",
        }

    def test_registration_success(self):
        response = self.client.post(self.url, self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="testuser").exists())
        self.assertRedirects(response, reverse("login"))

    def test_registration_password_mismatch(self):
        self.user_data["password2"] = "DifferentPassword"
        response = self.client.post(self.url, self.user_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, "form", "password2", "The two password fields didn't match."
        )

    def test_registration_username_taken(self):
        User.objects.create_user(username="testuser", password="SecurePassword123!")
        response = self.client.post(self.url, self.user_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, "form", "username", "A user with that username already exists."
        )
