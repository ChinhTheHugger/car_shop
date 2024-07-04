from rest_framework import serializers
from shop.models.request import Request

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'