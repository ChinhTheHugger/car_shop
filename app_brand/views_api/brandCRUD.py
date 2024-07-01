from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app_brand.models.brand import Brand
from app_brand.serializers.brand import BrandSerializer
import json

class BrandList(APIView):

    # 1. List all
    def get(self, request):
        brands = Brand.get_all_brands()
        serializer = BrandSerializer(brands, many=True)
        
        # this is how you extract data from the api response
        
        # results = Response(serializer.data, status=status.HTTP_200_OK).data
        # print(results)
        # print(results[0])
        # print(results[0]['brand'])
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BrandCreate(APIView):

    # 2. Create
    def post(self, request, format=None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Saved")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BrandGet(APIView):
    
    # 3. Retrieve
    def get(self, request, brandname):
        brand = Brand.get_brand(brandname)
        serializer = BrandSerializer(brand)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BrandUpdate(APIView):
    
    # 4. Update
    def put(self, request, brandname, format=None):
        brand = Brand.get_brand(brandname)
        serializer = BrandSerializer(brand, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, brandname, format=None):
        brand = Brand.get_brand(brandname)
        serializer = BrandSerializer(brand, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BrandDelete(APIView):
    
    # 5. Delete
    def delete(self, request, brandname):
        brand = Brand.get_brand(brandname)
        serializer = BrandSerializer(brand)
        if serializer.is_valid():
            Brand.remove_brand(brandname)
            return Response(status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)