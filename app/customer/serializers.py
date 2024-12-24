"""
Serializers for the Customer (tenant) API view.
"""

from django.utils.translation import gettext as _

from rest_framework import serializers
from core.models import Customer


class CustomerSerialzer(serializers.ModelSerializer):
    """Serializer for Customer objects"""

    # meta class descripts the model
    class Meta:
        model = Customer
        # These fields we want to be available in the serializer.
        # Only allow fields that you want the users to be able to change
        fields = '__all__'


    def create(self, validated_data):
        """Create and return a user with encrypted password.
        Overrides the default create method so that we can use
        our creat_user method that encrypts the pw"""
        return Customer().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with the provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
