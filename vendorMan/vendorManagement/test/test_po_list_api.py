# from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient
# from rest_framework.authtoken.models import Token
#
# from ..models import Vendor, PurchaseOrder
# from ..serializers import PurchaseOrderSerializer
#
#
# class TestPOListAPI(APITestCase):
#     """
#     Test suite to list purchase orders.
#
#     po_number = models.CharField(unique=True, max_length=255)
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     order_date = models.DateTimeField
#     delivery_date = models.DateTimeField
#     items = models.JSONField(default=dict)
#     quantity = models.IntegerField(default=1)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
#     quality_rating = models.FloatField(null=True, blank=True)
#     issue_date = models.DateTimeField
#     acknowledgment_date = models.DateTimeField(blank=True)
#     """
#
#     def setUp(self):
#
#         self.user = User.objects.create_user(username='admin', password='admin123')
#
#         self.vendor_1 = Vendor.objects.create(name="Vendor1", vendor_code="v1")
#         self.vendor_2 = Vendor.objects.create(name="Vendor2", vendor_code="v2")
#
#         self.po_1 = PurchaseOrder.objects.create(po_number="PO1", delivery_date=timezone.now(), )
#
#         self.user_token = Token.objects.create(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_token}')
#
#     def test_vendor_list_api(self):
#
#         response = self.client.get('/api/vendors/')
#         vendors = Vendor.objects.all()
#         vendor_serializer = VendorSerializer(vendors, many=True)
#
#         self.assertEquals(response.status_code, status.HTTP_200_OK)
#         self.assertEquals(response.data, vendor_serializer.data)
#
#     def test_vendor_list_api_without_authorization(self):
#         self.client.credentials(HTTP_AUTHORIZATION='')
#         response = self.client.get(f'/api/vendors/')
#
#         self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
#
#     def tearDown(self):
#         pass
#
#
