from django.urls import path
from .views import (
	ItemListCreateView, ItemRetrieveUpdateDestroyView, CategoryListCreateView, CategoryRetrieveUpdateDestroyView,
	ElectronicsItemListView, ClothingItemListView, StationaryItemListView, CredentialsItemListView, PetsItemListView
)

urlpatterns = [
	path('items/', ItemListCreateView.as_view(), name='item-list-create'),
	path('items/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item-retrieve-update-destroy'),
	path('category/', CategoryListCreateView.as_view(), name='category-list-create'),
	path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
	path('electronics/items/', ElectronicsItemListView.as_view(), name='electronics-item-list'),
	path('pets/items/', PetsItemListView.as_view(), name='pets-item-list'),
	path('credentials/items/', CredentialsItemListView.as_view(), name='credentials-item-list'),
	path('clothing/items/', ClothingItemListView.as_view(), name='clothing-item-list'),
	path('stationary/items/', StationaryItemListView.as_view(), name='stationary-item-list')
# 	path('electronics/', ElectronicListCreateView.as_view(), name='electronics-list-create'),
# 	path('electronics/<int:pk>/', ElectronicRetrieveUpdateDestroyView.as_view(), name='electronics-retrieve-update-destroy'),
# 	path('credentials/', CredentialListCreateView.as_view(), name='credential-list-create'),
# 	path('credentials/<int:pk>/', CredentialRetrieveUpdateDestoryView.as_view(), name='credentials-retrieve-update-destroy'),
# 	path('clothings/', ClothingListCreateView.as_view(), name='clothing-list-create'),
# 	path('clothings/<int:pk>/', ClothingRetrieveUpdateDestoryView.as_view(), name='clothing-retrieve-update-destroy'),
# 	path('furniture/', FurnitureListCreateView.as_view(), name='furniture-list-create'),
# 	path('furniture/<int:pk>/', FurnitureRetrieveUpdateDestoryView.as_view(), name='furniture-retrieve-update-destroy'),
# 	path('stationary/', StationaryListCreateView.as_view(), name='stationary-list-create'),
# 	path('stationary/<int:pk>/', StationaryRetrieveUpdateDestoryView.as_view(), name='stationary-retrieve-update-destroy'),
# 	path('pets/', PetListCreateView.as_view(), name='pet-list-create'),
# 	path('pets/<int:pk>/', PetRetrieveUpdateDestoryView.as_view(), name='pets-retrieve-update-destroy'),
#
]
