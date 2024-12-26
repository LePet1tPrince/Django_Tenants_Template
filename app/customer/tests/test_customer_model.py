"""Test the customer (tenant) functionality """
from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from core.models import Customer, Domain

from customer.serializers import CustomerSerialzer, DomainSerializer

CUSTOMER_URL = reverse('customer:customer-list')

def detail_url(customer_id):
    """Return customer detail URL"""
    return reverse('customer:customer-detail', args=[customer_id])

def create_customer(**params):
    """Create a sample customer"""
    defaults = {
        'schema_name': 'test',
        'name': 'Test Customer',
        'on_trial': True,
        'paid_until': '2023-01-01'
    }
    defaults.update(params)

    return Customer.objects.create(**defaults)


class CustomerAPITests(TenantTestCase):
    """Test the customer API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_customers(self):
        Customer.objects.create(schema_name="test",
                        name="Test Customer",
                        on_trial=True,
                        paid_until="2023-01-01")
        Customer.objects.create(schema_name="test2",
                        name="Test Customer2",
                        on_trial=True,
                        paid_until="2023-01-01")

        res = self.client.get(CUSTOMER_URL)

        customers = Customer.objects.all().order_by('-name')
        serializer = CustomerSerialzer(customers, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
