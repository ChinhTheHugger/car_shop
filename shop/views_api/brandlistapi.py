from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app_brand.models.brand import Brand
from shop.serializers.brand import BrandSerializer


class BrandListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        cars = Brand.get_all_brands()
        serializer = BrandSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'brandname': request.data.get('brandname'),
            'website': request.data.get('request'),
            'desintext': request.data.get('desintext'),
            'brandlogo': request.data.get('brandlogo')
        }
        serializer = BrandSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)