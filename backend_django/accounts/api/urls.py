from django.urls import path
from .views import UserLoginView, UserRegistrationView

urlpatterns = [
	path('sign up/', UserRegistrationView.as_view(), name='user-registration'),
	path ('login/', UserLoginView.as_view(), name='user-login')
]
