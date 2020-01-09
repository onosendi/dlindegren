from django.test import SimpleTestCase


class IndexViewTestCase(SimpleTestCase):
    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
