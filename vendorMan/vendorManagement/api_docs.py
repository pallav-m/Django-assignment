from drf_yasg import openapi
from rest_framework import status
from .serializers import VendorSerializer


def vendor_list_api_schema():

    return {
        'tags': ['Vendors'],
        'manual_parameters': None,
        'responses': {
            status.HTTP_200_OK: VendorSerializer,
            status.HTTP_400_BAD_REQUEST: 'Bad Request or Validation Error(s)',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden'
        },
        'operation_summary': 'List vendors',
        'operation_description': '',
    }