from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Customer

@admin.register(Customer)
class CustomerAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name', 'paid_until')