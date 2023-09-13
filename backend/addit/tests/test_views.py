from django.test import TestCase
from django.urls import reverse


class ViewTest(TestCase):
    fixtures = ["addit/tests/users.json"]

    def test_landing_page_as_anonymous(self):
        response = self.client.get(reverse("addit:landing-page"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("addit:landing-page"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, "/login/?next=/")

    def test_login_redirect(self):
        base_url = reverse("addit:login")
        response = self.client.post(base_url, {"username": "normal", "password": "123"}, follow=True)
        self.assertRedirects(response, reverse("addit:landing-page"))
        url = base_url + "?next=/"
        response = self.client.post(url, {"username": "normal", "password": "123"}, follow=True)
        self.assertRedirects(response, reverse("addit:landing-page"))
        url = base_url + "?next=/quote/hearts/"
        response = self.client.post(url, {"username": "normal", "password": "123"}, follow=True)
        self.assertEqual(response.request.get("PATH_INFO"), reverse("addit:quote-detail", args=["hearts"]))

    def test_landing_page_as_users(self):
        self.client.login(username="normal", password="123")
        response = self.client.get(reverse("addit:landing-page"))
        self.assertEqual(response.status_code, 200)
        self.client.login(username="admin", password="123")
        response = self.client.get(reverse("addit:landing-page"))
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        self.client.login(username="normal", password="123")
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("admin:index"), follow=True)
        self.assertRedirects(response, "/admin/login/?next=/admin/")
        self.client.login(username="admin", password="123")
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)
