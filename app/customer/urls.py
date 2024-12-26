"""
URL mappings for the customer (tenants) app
"""

from django.urls import (
    path,
    include
)

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('customer', views.CustomerViewSet)
router.register('domain', views.DomainViewSet)


app_name = 'customer'

urlpatterns = [
    path('', include(router.urls))

]