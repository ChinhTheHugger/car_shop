from rest_framework import serializers
from app_request.models.request import Request

class requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'