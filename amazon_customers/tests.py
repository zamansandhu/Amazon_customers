from django.test import TestCase, Client
from rest_framework.test import APITestCase


class TestCutomersApi(APITestCase):

    def test_for_customer(self):
        """Create New Customer"""
        c = Client()
        res_post = c.post('/amazon_customer/customer/', data={
            'customer_id': 4,
            'customer_name': 'zaman',
            'customer_phone': +9234333737373,
            'customer_email': 'abcd@gmail.com',
            'other_customer_details': 'hsahsajhsshaiwuuwweu'

        }, follow=True)

        customer_id = str(res_post.data['customer_id'])
        self.assertEqual(res_post.status_code, 201)

        """Fetch all customer"""

        res_get = c.get('/amazon_customer/customer/')
        self.assertEqual(res_get.status_code, 200)

        """Update artist"""
        data = '{"customer_name": "ali"}'
        res_update = c.patch("/amazon_customer/customer/" + customer_id + "/", data=data,
                             content_type="application/json")
        self.assertEqual(res_update.status_code, 200)

        """Delete artist"""
        res_delete = c.delete('amazon_customer/customer/' + customer_id + '/')
        self.assertEqual(res_delete.status_code, 404)

    def test_for_Ref_Payment_Method(self):
        c = Client()
        res_post = c.post('/amazon_customer/RPM/', data={
            'payment_method_code': 4,
            'payment_method_description': 'AM',
        }, follow=True)

        payment_method_code = str(res_post.data['payment_method_code'])
        self.assertEqual(res_post.status_code, 201)

        """Fetch all Data"""

        res_get = c.get('/amazon_customer/RPM/')
        self.assertEqual(res_get.status_code, 200)

        """Update artist"""
        data = '{"payment_method_description": "CSH"}'
        res_update = c.put("/amazon_customer/RPM/" + payment_method_code + "/", data=data,
                             content_type="application/json")
        self.assertEqual(res_update.status_code, 400)

        """Delete artist"""
        res_delete = c.delete('amazon_customer/RPM/' + payment_method_code + '/')
        self.assertEqual(res_delete.status_code, 404)
