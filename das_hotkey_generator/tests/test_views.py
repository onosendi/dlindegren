from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse


class IndexViewTestCase(SimpleTestCase):
    def test_index_page_status_code(self):
        response = self.client.get('/misc/das-hotkey-generator')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('das_hotkey_generator:index'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('das_hotkey_generator:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'das_hotkey_generator/index.html')
