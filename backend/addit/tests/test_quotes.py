from django.test import TestCase
from django.urls import reverse


class QuoteTest(TestCase):
    fixtures = ["addit/tests/users.json", "addit/tests/quotes.json"]

    def setUp(self):
        self.client.login(username="normal", password="123")

    def test_quotes(self):
        response = self.client.get(reverse("addit:quote-detail", args=["hearts"]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("addit:quote-detail", args=["does_not_exist"]))
        self.assertEqual(response.status_code, 404)

    def test_random_quote(self):
        response = self.client.post(reverse("addit:landing-page"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.get("PATH_INFO"), "/quote/hearts/")
