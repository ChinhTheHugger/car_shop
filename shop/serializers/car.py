from rest_framework import serializers
from app_car.models.car import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'