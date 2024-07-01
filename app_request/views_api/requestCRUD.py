from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app_request.models.request import Request
from app_request.serializers.request import RequestSerializer
import json

class RequestList(APIView):

    # 1. List all
    def get(self, request):
        requests = Request.get_all_requests()
        serializer = RequestSerializer(requests, many=True)
        
        # this is how you extract data from the api response
        
        # results = Response(serializer.data, status=status.HTTP_200_OK).data
        # print(results)
        # print(results[0])
        # print(results[0]['brand'])
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RequestCreate(APIView):

    # 2. Create
    def post(self, request, format=None):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Saved")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RequestGet(APIView):
    
    # 3. Retrieve
    def get(self, request, customerusername):
        request = Request.get_requests_by_customer(customerusername)
        serializer = RequestSerializer(request)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RequestUpdate(APIView):
    
    # 4. Update
    def put(self, request, customerusername, format=None):
        request = Request.get_requests_by_customer(customerusername)
        serializer = RequestSerializer(request, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, customerusername, format=None):
        request = Request.get_requests_by_customer(customerusername)
        serializer = RequestSerializer(request, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RequestDelete(APIView):
    
    # 5. Delete
    def delete(self, request, customerusername, car):
        request = Request.get_requests_by_customer(customerusername)
        serializer = RequestSerializer(request)
        if serializer.is_valid():
            Request.remove_request(car,customerusername)
            return Response(status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)