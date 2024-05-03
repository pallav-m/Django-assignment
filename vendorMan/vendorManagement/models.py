from django.db import models


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField(blank=True)
    address = models.TextField(blank=True)
    vendor_code = models.CharField(unique=True, max_length=255)
    on_time_delivery_rate = models.FloatField(blank=True)
    average_response_time = models.FloatField(blank=True)
    fulfillment_rate = models.FloatField(blank=True)

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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField
    acknowledgment_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.po_number


class HistPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.vendor
