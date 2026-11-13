import unittest
from app import app


class TestApp2(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_unknown_route_returns_404(self):
        response = self.client.get('/inconnu')
        self.assertEqual(response.status_code, 404)

    def test_hello_get_not_allowed(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 405)

    def test_hello_only_spaces(self):
        response = self.client.post('/hello', data={'username': '   '})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello there', response.data)

    def test_sum_negative_number(self):
        response = self.client.post('/sum', data={'a': '-2', 'b': '5'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'3.0', response.data)

    def test_sum_decimal_numbers(self):
        response = self.client.post('/sum', data={'a': '1.5', 'b': '2.25'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'3.75', response.data)


if __name__ == "__main__":
    unittest.main()
