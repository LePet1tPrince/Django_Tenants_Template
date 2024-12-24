from datetime import datetime
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django_tenants.models import TenantMixin, DomainMixin




class Customer(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

class Domain(DomainMixin):
    pass

class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a new user"""
        if not email:
            raise ValueError('Users must have an email address')

        if not extra_fields.get('customer'):
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            name = extra_fields.get('name')
            tenant = Customer.objects.create(
                schema_name=f'{email}-{timestamp}',
                name=name,
                paid_until='2022-12-05',
                on_trial=False)
            tenant.save()
            extra_fields['customer'] = tenant
            domain = Domain()
            domain.domain = 'localhost'
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()


        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in our system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'email'