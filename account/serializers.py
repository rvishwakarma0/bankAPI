from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'acc_type', 'balance', 'created', 'updated']
