from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import Account
from .serializers import AccountSerializer, LoginSerializer
from django.contrib.auth import authenticate
import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed


class UserRegistrationView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        #print(f'email:{email}, password: {password}')

        #user = authenticate(email=email, password=password)
        #print(f'Authenticated user: {user}')
        user = Account.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')
            #token, created = Token.objects.get_or_create(user=user)
            #return Response({'token': token.key, 'user_id': user.id, 'username': user.username})
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        # else:
        #     return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        #error should be here
        payload = {
            'id': user.id,
            'email': email,
            'password': password,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt':token
        }
        return response

class UserView(generics.CreateAPIView):
    serializer_class = AccountSerializer

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = Account.objects.filter(id=payload['id']).first()
        serializer = AccountSerializer(user)

        return Response(serializer.data)


class UserLogoutView(generics.DestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated]

    # def delete(self, request, *args, **kwargs):
    #     request.auth.delete()
    #     return Response(status=status.HTTP_200_OK)
    def post (self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
