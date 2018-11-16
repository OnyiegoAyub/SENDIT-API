
import unittest
import json
from app import create_app


class TestUserCase(unittest.TestCase):

  def setUp(self):

    create_app().testing = True #???
    '''create an instance of a flask application just as you would create  a flask app, but in this case you pass to it a test client which means you are running a test instance'''
    self.app = create_app().test_client() #???
    self.data = {
        "user_id": 1,
        "username": "Ayub",
        "role": "Admin",
        "email": "ayub@gmail.com",
        "password": "ayub"

    }