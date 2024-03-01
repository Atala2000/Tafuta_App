from rest_framework import serializers
from ..models import Account

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields  = ['id','username', 'email', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField(style={'input_type':'password'}, trim_whitespace=False)
