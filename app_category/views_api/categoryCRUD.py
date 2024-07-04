from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from shop.models.category import Category
from app_category.serializers.category import CategorySerializer
import json

class CategoryList(APIView):

    # 1. List all
    def get(self, request):
        categorys = Category.get_all_categories()
        serializer = CategorySerializer(categorys, many=True)
        
        # this is how you extract data from the api response
        
        # results = Response(serializer.data, status=status.HTTP_200_OK).data
        # print(results)
        # print(results[0])
        # print(results[0]['brand'])
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryCreate(APIView):

    # 2. Create
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Saved")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryGet(APIView):
    
    # 3. Retrieve
    def get(self, request, categoryname):
        category = Category.get_category_by_name(categoryname)
        serializer = CategorySerializer(category)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryUpdate(APIView):
    
    # 4. Update
    def put(self, request, categoryname, format=None):
        category = Category.get_category_by_name(categoryname)
        serializer = CategorySerializer(category, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, categoryname, format=None):
        category = Category.get_category_by_name(categoryname)
        serializer = CategorySerializer(category, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryDelete(APIView):
    
    # 5. Delete
    def delete(self, request, categoryname):
        category = Category.get_category_by_name(categoryname)
        serializer = CategorySerializer(category)
        if serializer.is_valid():
            Category.remove_category(categoryname)
            return Response(status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)