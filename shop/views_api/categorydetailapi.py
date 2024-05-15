from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from app_category.models.category import Category
from shop.serializers.category import CategorySerializer

class CategoryDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, category):
        '''
        Helper method to get the object with given Category_id, and user_id
        '''
        try:
            return Category.get_category_by_name(category)
        except Category.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, category, *args, **kwargs):
        '''
        Retrieves the Category with given Category_id
        '''
        Category_instance = self.get_object(category)
        if not Category_instance:
            return Response(
                {"res": "Object with Category id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CategorySerializer(Category_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, category, *args, **kwargs):
        '''
        Updates the Category item with given Category_id if exists
        '''
        Category_instance = self.get_object(category)
        if not Category_instance:
            return Response(
                {"res": "Object with Category id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'categoryname': request.data.get('categoryname'),
            'categoryimage': request.data.get('categoryimage')
        }
        serializer = CategorySerializer(instance = Category_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, category, *args, **kwargs):
        '''
        Deletes the Category item with given Category_id if exists
        '''
        Category_instance = self.get_object(category)
        if not Category_instance:
            return Response(
                {"res": "Object with Category id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        Category_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )