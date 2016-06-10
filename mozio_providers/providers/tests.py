import json
from rest_framework.test import APITestCase
from rest_framework import status

from django.core.urlresolvers import reverse

from .models import Provider


class ProviderAPITests(APITestCase):
    data = {
        "name": "World Service",
        "email": "ws@gmail.com",
        "phone_no": "+9779841157853",
        "language": "en",
        "currency": "USD"
    }

    def test_provider_successfully_created(self):
        url = reverse('api_providers:provider_collection')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Provider.objects.count(), 1)
        self.assertEqual(Provider.objects.get().name, self.data["name"])
        self.assertEqual(Provider.objects.get().email, self.data["email"])
        self.assertEqual(Provider.objects.get().language, self.data["language"])
        self.assertEqual(Provider.objects.get().currency, self.data["currency"])

    def test_error_wrong_language(self):
        url = reverse('api_providers:provider_collection')
        newdata = self.data.copy()
        newdata["language"] = "Dummy language"
        response = self.client.post(url, newdata, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_error_wrong_currency(self):
        url = reverse('api_providers:provider_collection')
        newdata = self.data.copy()
        newdata["currency"] = "Dummy currency"
        response = self.client.post(url, newdata, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_error_wrong_email(self):
        url = reverse('api_providers:provider_collection')
        newdata = self.data.copy()
        newdata["email"] = "Dummy email"
        response = self.client.post(url, newdata, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_api(self):
        url = reverse('api_providers:provider_collection')
        self.client.post(url, self.data, format='json')
        response = self.client.get(url, format='json')
        self.assertEqual(len(json.loads(response.content.decode('utf-8'))), 1)
