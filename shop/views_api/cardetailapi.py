from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app_car.models.car import Car
from shop.serializers.car import CarSerializer

class CarDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, brand, model, year):
        '''
        Helper method to get the object with given Car_id, and user_id
        '''
        try:
            return Car.get_car(brand,model,year)
        except Car.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, brand, model, year, *args, **kwargs):
        '''
        Retrieves the Car with given Car_id
        '''
        Car_instance = self.get_object(brand,model,year)
        if not Car_instance:
            return Response(
                {"res": "Object with Car id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CarSerializer(Car_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, brand, model, year, *args, **kwargs):
        '''
        Updates the Car item with given Car_id if exists
        '''
        Car_instance = self.get_object(brand,model,year)
        if not Car_instance:
            return Response(
                {"res": "Object with Car id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
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
        serializer = CarSerializer(instance = Car_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, brand, model, year, *args, **kwargs):
        '''
        Deletes the Car item with given Car_id if exists
        '''
        Car_instance = self.get_object(brand,model,year)
        if not Car_instance:
            return Response(
                {"res": "Object with Car id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        Car_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )