from rest_framework import serializers
from app_brand.models.brand import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Mera:
        model = Brand
        fields = '__all__'