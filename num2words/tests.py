from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class NumToEnglishAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_num_to_english_get(self):
        response = self.client.get(reverse('num_to_english'), {'number': '12345678'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')
        self.assertEqual(response.data['num_in_english'], 'twelve million three hundred forty-five thousand six hundred seventy-eight')

    def test_num_to_english_post(self):
        data = {'number': '87654321'}
        response = self.client.post(reverse('num_to_english'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')
        self.assertEqual(response.data['num_in_english'], 'eighty-seven million six hundred fifty-four thousand three hundred twenty-one')

    def test_invalid_number_format(self):
        data = {'number': 'abc'}
        response = self.client.post(reverse('num_to_english'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['status'], 'error')
        self.assertEqual(response.data['message'], 'Invalid number format')

    def test_missing_number_parameter(self):
        response = self.client.get(reverse('num_to_english'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['status'], 'error')
        self.assertEqual(response.data['message'], 'Number parameter is missing')
