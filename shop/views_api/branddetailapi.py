from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app_brand.models.brand import Brand
from shop.serializers.brand import BrandSerializer

class BrandDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, brand):
        '''
        Helper method to get the object with given Brand_id, and user_id
        '''
        try:
            return Brand.get_brand_by_name(brand)
        except Brand.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, brand, *args, **kwargs):
        '''
        Retrieves the Brand with given Brand_id
        '''
        Brand_instance = self.get_object(brand)
        if not Brand_instance:
            return Response(
                {"res": "Object with Brand id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BrandSerializer(Brand_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, brand, *args, **kwargs):
        '''
        Updates the Brand item with given Brand_id if exists
        '''
        Brand_instance = self.get_object(brand)
        if not Brand_instance:
            return Response(
                {"res": "Object with Brand id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'brandname': request.data.get('brandname'),
            'website': request.data.get('request'),
            'desintext': request.data.get('desintext'),
            'brandlogo': request.data.get('brandlogo')
        }
        serializer = BrandSerializer(instance = Brand_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, brand, *args, **kwargs):
        '''
        Deletes the Brand item with given Brand_id if exists
        '''
        Brand_instance = self.get_object(brand)
        if not Brand_instance:
            return Response(
                {"res": "Object with Brand id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        Brand_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )