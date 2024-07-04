from rest_framework import serializers
from shop.models.brand import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Mera:
        model = Brand
        fields = '__all__'