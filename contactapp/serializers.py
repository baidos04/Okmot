from rest_framework import serializers
from .models import ContInfo, Feedback


class ContInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContInfo
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'