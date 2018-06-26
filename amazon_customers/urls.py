from django.urls import path
from rest_framework import routers
from .views import Ref_Payment_MethodsViewSet, CustomersViewSet,AddressesViewSet, Ref_Address_typeViewSet, Customer_Payment_MethodsViewSet,Customer_AddressesViewSet

router = routers.DefaultRouter()

router.register('RPM', Ref_Payment_MethodsViewSet)
router.register('customer', CustomersViewSet)
router.register('addresses', AddressesViewSet)
router.register('RDT', Ref_Address_typeViewSet)
router.register('CPM', Customer_Payment_MethodsViewSet)
router.register('customeraddress', Customer_AddressesViewSet)

urlpatterns = router.urls

