from django.contrib import admin

# Register your models here.
from amazon_customers.models import Ref_Pyament_Methods, Customers, Addresses,Ref_Address_type, Customer_Payment_Methods, Customer_Addresses

admin.site.register(Ref_Pyament_Methods)
admin.site.register(Customers)
admin.site.register(Addresses)
admin.site.register(Ref_Address_type)
admin.site.register(Customer_Payment_Methods)
admin.site.register(Customer_Addresses)