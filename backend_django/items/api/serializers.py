from rest_framework import serializers
from ..models import Item, Electronic, Clothing, Credential, Pet, Stationary, Furniture

class ElectronicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electronic
        fields = '__all__'

class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = '__all__'

class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class StationarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Stationary
        fields = '__all__'

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    #electronic = ElectronicSerializer(read_only=True)
    #clothing = ClothingSerializer(read_only=True)
    #credential = CredentialSerializer(read_only=True)
    #pet = PetSerializer(read_only=True)
    #stationary = StationarySerializer(read_only=True)
    #furniture = FurnitureSerializer(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
