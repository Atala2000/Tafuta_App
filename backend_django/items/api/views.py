from rest_framework import generics
from ..models import Item, Electronic, Credential, Clothing, Stationary, Furniture, Pet
from .serializers import ItemSerializer, ElectronicSerializer,ClothingSerializer, CredentialSerializer, StationarySerializer, FurnitureSerializer, PetSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    #def get_queryset(self):
    #    queryset = super().get_queryset()
    #   search_query = self.request.query_params.get('search', None)

    #   if search_query:
    #       queryset = queryset.filter(name__icontains=search_query)

    #    return queryset


class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ElectronicListCreateView(generics.ListCreateAPIView):
    queryset = Electronic.objects.all()
    serializer_class = ElectronicSerializer

class ElectronicRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Electronic.objects.all()
    serializer_class = ElectronicSerializer

class CredentialListCreateView(generics.ListCreateAPIView):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer

class CredentialRetrieveUpdateDestoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer

class ClothingListCreateView(generics.ListCreateAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer

class ClothingRetrieveUpdateDestoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer

class StationaryListCreateView(generics.ListCreateAPIView):
    queryset = Stationary.objects.all()
    serializer_class = StationarySerializer

class StationaryRetrieveUpdateDestoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stationary.objects.all()
    serializer_class = StationarySerializer

class FurnitureListCreateView(generics.ListCreateAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer

class FurnitureRetrieveUpdateDestoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer

class PetListCreateView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetRetrieveUpdateDestoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
