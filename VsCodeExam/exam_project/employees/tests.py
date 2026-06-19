from django.test import TestCase, Client
class Testing(TestCase):
    def test_ping(self):
        client = Client()
        response = client.get('/ping/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'ok'})