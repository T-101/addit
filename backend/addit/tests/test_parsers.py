from django.test import TestCase
from addit.templatetags.www_extras import parse_quote


class QuoteTest(TestCase):

    def test_hearts(self):
        test = parse_quote("<3")
        self.assertEqual(test, '<i class="fa-solid fa-heart"></i>')

    def test_multiline(self):
        test = parse_quote("<@user1> one <user2> two")
        self.assertEqual(test, "<strong>&lt;@user1&gt;</strong> one\n <strong>&lt;user2&gt;</strong> two")

    def test_urls(self):
        test = parse_quote("http://localhost:8000/")
        self.assertEqual(test, '<a href="http://localhost:8000/">http://localhost:8000/</a>')
        test = parse_quote("https://example.com")
        self.assertEqual(test, '<a href="https://example.com">https://example.com</a>')
