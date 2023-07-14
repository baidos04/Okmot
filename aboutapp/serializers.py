from rest_framework import serializers
from .models import History, AdminContact, Deputies

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class AdminContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminContact
        fields = '__all__'

class DeputiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deputies
        fields = '__all__'
