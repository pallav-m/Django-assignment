from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Vendor, PurchaseOrder, HistPerformance
from .serializers import VendorSerializer


# Create your views here.

class VendorView(APIView):

    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        data = {
            'name' : request.data.get('name'),
            'contact_details' : request.data.get('contact_details'),
            'address' : request.data.get('address'),
            'vendor_code' : request.data.get('vendor_code'),
            'on_time_delivery_rate' : request.data.get('on_time_delivery_rate'),
            'average_response_time' : request.data.get('average_response_time'),
            'fulfillment_rate' : request.data.get('fulfillment_rate'),
        }
        serializer = VendorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class VendorDetailView(APIView):

    def get_vendor(self, vendor_id):
        '''
        get vendor by vendor_id if it exists
        '''

        try:
            return Vendor.objects.get(vendor_id=vendor_id)
        except Vendor.DoesNotExist:
            return None

    def get(self, request, vendor_id, *args, **kwargs):

        vendor_instance = self.get_vendor(vendor_id)
        if not vendor_instance:
            return Response(
                {'response': 'Vendor does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = VendorSerializer(vendor_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, vendor_id, *args, **kwargs):

        vendor_instance = self.get_vendor(vendor_id)
        if not vendor_instance:
            return Response(
                {'response': 'Vendor does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )
        data = {
            'name': request.data.get('name'),
            'contact_details': request.data.get('contact_details'),
            'address': request.data.get('address'),
            'vendor_code': request.data.get('vendor_code'),
            'on_time_delivery_rate': request.data.get('on_time_delivery_rate'),
            'average_response_time': request.data.get('average_response_time'),
            'fulfillment_rate': request.data.get('fulfillment_rate'),
        }
        serializer = VendorSerializer(vendor_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)