from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class APITest(TestCase):
    fixtures = ["addit/tests/users.json", "addit/tests/quotes.json"]

    def test_anonymous_user(self):
        response = self.client.get("/v1/")
        self.assertEqual(response.status_code, 404)
        response = self.client.get("/v1/rexpl/")
        self.assertEqual(response.status_code, 401)
        response = self.client.get("/v1/quotes/a53a6059-c7eb-49b2-bf97-844fda6df635/")
        self.assertEqual(response.status_code, 401)

    def test_normal_user(self):
        self.client.login(username="normal", password="123")
        response = self.client.get("/v1/")
        self.assertEqual(response.status_code, 404)
        response = self.client.get("/v1/rexpl/")
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/v1/quotes/a53a6059-c7eb-49b2-bf97-844fda6df635/")
        self.assertEqual(response.status_code, 200)

    def test_admin_user(self):
        self.client.login(username="admin", password="123")
        response = self.client.get("/v1/")
        self.assertEqual(response.status_code, 404)
        response = self.client.get("/v1/rexpl/")
        self.assertEqual(response.status_code, 200)

    def test_token(self):
        token = Token.objects.get(user__pk=2)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get("/v1/")
        self.assertEqual(response.status_code, 404)
        response = client.get("/v1/rexpl/")
        self.assertEqual(response.status_code, 200)
        response = client.get("/v1/quotes/a53a6059-c7eb-49b2-bf97-844fda6df635/")
        self.assertEqual(response.status_code, 200)

    def test_quote(self):
        self.client.login(username="normal", password="123")
        response = self.client.get("/v1/quotes/a53a6059-c7eb-49b2-bf97-844fda6df635/")
        json = response.json()
        self.assertEqual(json.get("handle"), "user1")
        self.assertEqual(json.get("content"), "<@user1> line <@user2> <3")
