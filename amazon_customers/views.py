from django.shortcuts import render
from rest_framework import viewsets

from .models import Ref_Pyament_Methods, Customers, Addresses, Ref_Address_type, Customer_Payment_Methods, \
    Customer_Addresses
from .serializers import Ref_Pyament_MethodsSerializers, CustomersSerializers, Ref_Address_typeSerializers, \
    Customer_Payment_MethodsSerializers, Customer_AddressesSerializers, AddressesSerializers


# Create your views here.
# @action(methods=['post', 'delete'], detail=True)
class Ref_Payment_MethodsViewSet(viewsets.ModelViewSet):
    queryset = Ref_Pyament_Methods.objects.all()
    serializer_class = Ref_Pyament_MethodsSerializers


# @action(methods=['post', 'delete'], detail=True)
class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializers


class AddressesViewSet(viewsets.ModelViewSet):
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializers


# @action(methods=['post', 'delete'], detail=True)
class Ref_Address_typeViewSet(viewsets.ModelViewSet):
    queryset = Ref_Address_type.objects.all()
    serializer_class = Ref_Address_typeSerializers


# @action(methods=['post', 'delete'], detail=True)
class Customer_Payment_MethodsViewSet(viewsets.ModelViewSet):
    queryset = Customer_Payment_Methods.objects.all()
    serializer_class = Customer_Payment_MethodsSerializers


# @action(methods=['post', 'delete'], detail=True)
class Customer_AddressesViewSet(viewsets.ModelViewSet):
    queryset = Customer_Addresses.objects.all()
    serializer_class = Customer_AddressesSerializers