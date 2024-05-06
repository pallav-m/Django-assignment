from .models import Vendor, PurchaseOrder, HistPerformance
from datetime import datetime


def delivery_rate(vendor_id: int) -> float:
    """Calculate the on-time delivery rate for purchase orders."""

    current_time = datetime.now()

    vendor_purchase_orders = Vendor.objects.filter(vendor=vendor_id, status='COMPLETED')
    vendor_on_time_delivered = vendor_purchase_orders.filter(delivery_date__lte=current_time)

    if vendor_purchase_orders.count() == 0:
        return 0
    delivery_rate_ratio = vendor_on_time_delivered.count() / vendor_purchase_orders.count()

    return delivery_rate_ratio


def quality_rating_average(vendor_id):
    """Calculate the quality rating of a vendor"""

    vendor_purchase_orders = Vendor.objects.filter(vendor=vendor_id, status='COMPLETED')
    vendor_rated_orders = vendor_purchase_orders.exclude(quality_rating=None)

    vendor_ratings = vendor_rated_orders.values('quality_rating')
    if vendor_rated_orders.count() == 0:
        return 0
    average_rating = vendor_ratings / vendor_rated_orders.count()

    return average_rating


def average_response_time(vendor_id):
    """Calculate the average response time for a purchase order"""
    vendor_purchase_orders = Vendor.objects.filter(vendor=vendor_id)

    time_diffs = []
    for order in vendor_purchase_orders:

        if not order.acknowledgment_date:
            time_diff = (order.acknowledgment_date - order.issue_date).total_seconds()
            time_diffs.append(time_diff)

    if len(time_diffs) == 0:
        return 0

    average_time_diff = sum(time_diffs) / len(time_diffs)

    return average_time_diff


def fulfillment_rate(vendor_id):
    """Calculate the fulfilment rate for successful orders"""
    vendor_purchase_orders = Vendor.objects.filter(vendor=vendor_id)
    successful_orders = vendor_purchase_orders.filter(status='COMPLETED')
    if vendor_purchase_orders.count() == 0:
        return 0

    rate = successful_orders.count() / vendor_purchase_orders.count()

    return rate

