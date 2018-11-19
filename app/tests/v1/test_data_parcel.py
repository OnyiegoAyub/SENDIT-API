import json
import unittest
from app import create_app


class TestParcelCase(unittest.TestCase):
    """
    Tests for parcel order methods defined in the app
    """

    def setUp(self):

        create_app().testing = True
        '''
        create an instance of a flask application just as you would create  a
        flask app, but in this case you pass to it a test client which means
        you are running a test instance
        '''
        self.app = create_app().test_client()
        self.data = {
            "parcel_id": 1,
            "user_id": 1,
            "origin": "Eldoret",
            "destination": "Kitale",
            "weight": 5,
            "status": "pending delivery"
            }

    def test_create_order(self):
        """ Tests for posting a parcel order"""
        response = self.app.post('/api/v1/parcels', data=json.dumps(self.data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_cancel_order(self):
        """ Tests for cancelling a parcel order"""
        response = self.app.put('api/v1/parcels/1/cancel')
        self.assertEqual(response.status_code, 202)

    def test_get_all_orders(self):
        """ Tests for getting all parcel orders"""
        response = self.app.get('api/v1/parcels')
        self.assertEqual(response.status_code, 200)

    def test_get_single_order(self):
        """ Tests forgetting a single parcel order"""
        response = self.app.get('api/v1/parcels/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
