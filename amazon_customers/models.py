from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

class Ref_Pyament_Methods(models.Model):
    PAYMENT_CHOICES = (
        ('AM', 'AmEx'),
        ('MC', 'MasterCard'),
        ('CSH', 'Cash')
    )
    payment_method_description = models.CharField(max_length=255, choices=PAYMENT_CHOICES)
    payment_method_code = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.payment_method_description


class Customers(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 20 digits allowed.")
    customer_phone = models.CharField(validators=[phone_regex], max_length=20)
    customer_email = models.CharField(max_length=50, unique=True, blank=True)
    other_customer_details = models.TextField()

class Addresses(models.Model):
    address_id = models.IntegerField(primary_key=True)
    line_1_number_bilding = models.CharField(max_length=255)
    line_2_number_street = models.CharField(max_length=255)
    line_3_area_locality = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_postcode = models.IntegerField()
    state = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    iso_country_code = models.IntegerField()
    other_address_details = models.TextField()


class Customer_Payment_Methods(models.Model):
    customer_payment_method_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    payment_method_code = models.ForeignKey(Ref_Pyament_Methods, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=150)
    date_from = models.DateField()
    date_to = models.DateField()
    other_details = models.TextField()


class Ref_Address_type(models.Model):
    address_type_code = models.CharField(max_length=150, primary_key=True)
    address_type_description = models.TextField()



class Customer_Addresses(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    date_from = models.ForeignKey(Customer_Payment_Methods, on_delete=models.CASCADE)
    address_type_code = models.ForeignKey(Ref_Address_type, on_delete=models.CASCADE)
    date_to = models.DateField()
