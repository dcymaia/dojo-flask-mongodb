import unittest
from app import my_app_web


class TestApp(unittest.TestCase):
    def test_app_home_url(self):
        app = my_app_web.test_client()
        self.response = app.get('/')
        self.assertEqual(200, self.response.status_code)

    def test_app_user_url(self):
        app = my_app_web.test_client()
        self.response = app.get('/user/dcymaia')
        self.assertEqual(200, self.response.status_code)


if __name__ == '__main__':
    unittest.main()
