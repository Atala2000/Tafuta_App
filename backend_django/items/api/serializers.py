from rest_framework import serializers
from ..models import Item, Category
import logging

# class ElectronicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Electronic
#         fields = '__all__'

# class ClothingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Clothing
#         fields = '__all__'

# class CredentialSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Credential
#         fields = '__all__'

# class PetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pet
#         fields = '__all__'

# class StationarySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Stationary
#         fields = '__all__'

# class FurnitureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Furniture
#         fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'category', 'category_name', 'location_found', 'date_found', 'image', 'owner','owner_username']


