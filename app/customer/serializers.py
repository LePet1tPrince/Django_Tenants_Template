"""
Serializers for the Customer (tenant) API view.
"""

from django.utils.translation import gettext as _

from rest_framework import serializers
from core.models import Customer, Domain



class CustomerSerialzer(serializers.ModelSerializer):
    """Serializer for Customer objects"""

    paid_until = serializers.DateField(input_formats=['%Y-%m-%d'])
    # meta class descripts the model
    class Meta:
        model = Customer
        # These fields we want to be available in the serializer.
        # Only allow fields that you want the users to be able to change
        # fields = ['id','schema_name','name','on_trial','paid_until']
        fields = '__all__'
        read_only_fields = ['id']


class DomainSerializer(serializers.ModelSerializer):
    """Serializer for Domain objects"""

    class Meta:
        model = Domain

        fields = ['domain', 'tenant', 'is_primary']
