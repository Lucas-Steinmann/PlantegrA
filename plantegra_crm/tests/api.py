from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from plantegra_crm.models import Customer, Appointment, Address
from plantegra_crm.serializers import AddressSerializer


class CustomerTests(APITestCase):

    def test_create_customer(self):
        """ Ensure we can create a new customer object. """
        url = reverse('customer-list')
        data = {'name': 'Herrenknecht'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'Herrenknecht')


class AppointmentTests(APITestCase):
    fixtures = ['herrenknecht_customer_and_location']

    def test_create_appointment(self):
        """ Ensure we can create a new customer object. """
        url = reverse('appointment-list')
        location = Address.objects.get(pk=1)
        data = {'description': 'Hecke schneiden',
                'location': AddressSerializer(location).data['url'],
                'start_date': '2019-01-01 12:00:00',
                'end_date': '2019-01-01 13:00:00'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(Appointment.objects.get().name, 'Hecke schneiden')

