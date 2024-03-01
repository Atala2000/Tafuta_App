from rest_framework import serializers
from ..models import Item, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    #owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'category', 'category_name', 'location_found', 'date_found', 'image', 'contact']

