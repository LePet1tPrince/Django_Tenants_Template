"""
Views for the user API
generics module gives a bunch of defaults
"""
from rest_framework import (
    generics,
    authentication,
    permissions,
    viewsets)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import (
    CustomerSerialzer,
    DomainSerializer
)
from core.models import Customer, Domain


class CustomerViewSet(viewsets.ModelViewSet):
    """Create a new Customer (tenant) in the system"""
    serializer_class = CustomerSerialzer
    queryset = Customer.objects.all()


class DomainViewSet(viewsets.ModelViewSet):
    """Create a new Domain  in the system"""
    serializer_class = DomainSerializer
    queryset = Domain.objects.all()