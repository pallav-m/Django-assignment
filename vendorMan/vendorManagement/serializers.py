from rest_framework import serializers
from .models import Vendor, PurchaseOrder


class VendorSerializer(serializers.Serializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class PurchaseOrderSerializer(serializers.Serializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
