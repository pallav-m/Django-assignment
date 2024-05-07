from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

from datetime import datetime


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    vendor_code = models.CharField(unique=True, max_length=255)
    on_time_delivery_rate = models.FloatField(blank=True, null=True)
    average_response_time = models.FloatField(blank=True, null=True)
    fulfillment_rate = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')
    )
    po_number = models.CharField(unique=True, max_length=255)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField
    delivery_date = models.DateTimeField
    items = models.JSONField(default=dict)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField
    acknowledgment_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.po_number


class HistPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.vendor


# @receiver(pre_save, sender=PurchaseOrder, dispatch_uid="purchase_order_analytics")
# def trigger_analytics(sender, instance, **kwargs):
#     existing_po = PurchaseOrder.objects.get(id=instance.id)
#     if existing_po.status != 'COMPLETED':
#         if instance.status == 'COMPLETED':
#             pass