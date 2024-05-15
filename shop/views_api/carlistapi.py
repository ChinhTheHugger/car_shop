from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app_car.models.car import Car
from shop.serializers.car import CarSerializer
import json


class CarListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        cars = Car.get_all_cars()
        serializer = CarSerializer(cars, many=True)
        
        # this is how you extract data from the api response
        
        # results = Response(serializer.data, status=status.HTTP_200_OK).data
        # print(results)
        # print(results[0])
        # print(results[0]['brand'])
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'brand': request.data.get('brand'),
            'model': request.data.get('model'),
            'year': request.data.get('year'),
            'category': request.data.get('category'),
            'desintext': request.data.get('desintext'),
            'front': request.data.get('front'),
            'back': request.data.get('back'),
            'interoir': request.data.get('interior'),
            'instock': request.data.get('instock'),
            'price': request.data.get('price')
        }
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)