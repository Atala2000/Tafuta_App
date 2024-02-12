from rest_framework import serializers
from ..models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        #fields = ['id', 'username', 'email', 'phone_number', 'is_active', 'is_staff', 'password']
        fields  = ['username', 'email', 'phone_number', 'password']
