
import unittest
import json
from app import create_app


class TestUserCase(unittest.TestCase):

    def setUp(self):

        create_app().testing = True
        '''create an instance of a flask application just as you would create
        a flask app, but in this case you pass to it a test client which means
         you are running a test instance'''
        self.app = create_app().test_client()
        self.data = {
            "user_id": 1,
            "username": "Ayub",
            "role": "Admin",
            "email": "ayub@gmail.com",
            "password": "ayub"}


    def test_create_user(self):
        """ Tests for creating new user"""
        response = self.app.post('/api/v1/users', data=json.dumps(self.data),
                                 content_type='application/json')
        results = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_create_user_success_message(self):
        """ Tests for ensuring message passed is correct"""
        response = self.app.post('/api/v1/users', data=json.dumps(self.data),
                                 content_type='application/json')
        results = json.loads(response.data.decode())
        self.assertEqual(results['message'], 'Successfully created account')

    def test_get_all_users(self):
        """ Tests for getting all users"""
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)

    def test_get_single_user(self):
        """ Tests getting single user"""
        response = self.app.get('/api/v1/users/1')
        self.assertEqual(response.status_code, 200)

    def test_get_user_not_registered(self):
        """ Test cannot get a non registerd user."""
        response = self.app.get('/api/v1/users/1')
        results = json.loads(response.data.decode())
        self.assertEqual(results['status'], 'Requested user does not exist')

if __name__ == '__main__':
    unittest.main()
