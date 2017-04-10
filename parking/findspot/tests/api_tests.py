"""
Unit test case for parking spot api
./manage.py test findspot.tests.api_tests
"""

from django.test import Client
from django.test import TestCase
from findspot.models import Space
import os
import json


class APITests(TestCase):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fixtures = [os.path.join(BASE_DIR, 'fixtures/seed_data.json')]

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        TestCase.tearDown(self)

    def test_list_available_parking_api(self):
        response = self.client.get("/spot/", {"lat": 1, "long": 1, "rad": 6})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), 6)

    def test_reserve_parking(self):
        obj = Space.objects.get(id=5)
        params = {"parking_slot": 5, "btime": 25}
        response = self.client.put('/spot/', json.dumps(params), 'application/json')
        self.assertTrue(obj.is_available)
        self.assertEqual(response.status_code, 202)
        obj = Space.objects.get(id=5)
        self.assertFalse(obj.is_available)