from rest_framework import generics, permissions
from ..models import Item, Category
from .serializers import ItemSerializer, CategorySerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'GET':
            return [permissions.AllowAny()]
        elif self.request.method == 'PUT':
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

    def create(self, serializers):
        serializers.save(owner=self.request.user)

class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ElectronicsItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        electronics_category = Category.objects.get(name='Electronics')
        return Item.objects.filter(category=electronics_category)

class CredentialsItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        credential_category = Category.objects.get(name='Credentials')
        return Item.objects.filter(category=credential_category)

class PetsItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        pet_category = Category.objects.get(name='Pets')
        return Item.objects.filter(category=pet_category)

class ClothingItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        clothing_category = Category.objects.get(name='Clothing')
        return Item.objects.filter(category=clothing_category)

class StationaryItemListView(generics.ListAPIView):
    serializer_class= ItemSerializer

    def get_queryset(self):
        stationary_category = Category.objects.get(name='Stationary')
        return Item.objects.filter(category=stationary_category)

