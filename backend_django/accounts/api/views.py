from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .. models import Account
from .serializers import AccountSerializer
#from rest_framework import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from django.http import JsonResponse


class UserRegistrationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args,  **kwargs):
        serializer =self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        #Token.objects.create(user=user)

        token, created = Token.objects.get_or_create(user=user)

        #print(token.key)

        return Response({'token': token.key, 'key_id': user.id}, status=status.HTTP_201_CREATED)

# disable csrf for this view
@method_decorator(csrf_exempt, name='dispatch')
class UserLoginView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AccountSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        print(f'Username: {username}, Password: {password}')


        if username is None or password is None:
            return JsonResponse({'error': 'Please provide both username and password'}, status=400)

        user = authenticate(request, username=username, password=password)
        print('Authenticated User:', user)
        print(f'Username: {username}, Password: {password}')


        if not user:
            return JsonResponse({'error': 'Invalid Credentials'}, status=401)

        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key, 'user_id':user.id})

