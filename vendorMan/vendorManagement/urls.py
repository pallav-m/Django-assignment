from django.urls import path, include
from .views import VendorView, VendorDetailView, PurchaseOrderView, PurchaseOrderDetailView, VendorPerformanceMetricsView

urlpatterns = [
    path('vendors/', VendorView.as_view()),
    path('vendors/<int:vendor_id>/', VendorDetailView.as_view()),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceMetricsView.as_view()),
    path('purchase_orders/', PurchaseOrderView.as_view()),
    path('purchase_orders/<int:po_id>/', PurchaseOrderDetailView.as_view()),
]