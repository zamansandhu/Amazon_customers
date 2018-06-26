from rest_framework import serializers
from .models import Ref_Pyament_Methods, Customers, Addresses, Ref_Address_type, Customer_Payment_Methods, \
    Customer_Addresses


class Ref_Pyament_MethodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ref_Pyament_Methods
        fields = '__all__'


class CustomersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class AddressesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = '__all__'


class Ref_Address_typeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ref_Address_type
        fields = '__all__'


class Customer_Payment_MethodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer_Payment_Methods
        fields = '__all__'


class Customer_AddressesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer_Addresses
        fields = '__all__'



