from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app_car.models.car import Car
from app_car.serializers.car import CarSerializer
import json

class CarList(APIView):

    # 1. List all
    def get(self, request):
        cars = Car.get_all_cars()
        serializer = CarSerializer(cars, many=True)
        
        # this is how you extract data from the api response
        
        # results = Response(serializer.data, status=status.HTTP_200_OK).data
        # print(results)
        # print(results[0])
        # print(results[0]['brand'])
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CarCreate(APIView):

    # 2. Create
    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Saved")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CarGet(APIView):
    
    # 3. Retrieve
    def get(self, request, brand, model, year):
        car = Car.get_car(brand,model,year)
        serializer = CarSerializer(car)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CarUpdate(APIView):
    
    # 4. Update
    def put(self, request, brand, model, year, format=None):
        car = Car.get_car(brand,model,year)
        serializer = CarSerializer(car, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, brand, model, year, format=None):
        car = Car.get_car(brand,model,year)
        serializer = CarSerializer(car, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CarDelete(APIView):
    
    # 5. Delete
    def delete(self, request, brand, model, year):
        car = Car.get_car(brand,model,year)
        serializer = CarSerializer(car)
        if serializer.is_valid():
            Car.remove_car(brand,model,year)
            return Response(status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)