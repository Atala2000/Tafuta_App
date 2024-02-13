from django.urls import path
from .views import UserLoginView, UserRegistrationView, UserLogoutView

urlpatterns = [
	path('sign up/', UserRegistrationView.as_view(), name='user-registration'),
	path ('login/', UserLoginView.as_view(), name='user-login'),
	path ('logout/', UserLogoutView.as_view(), name='user-logout')
]
