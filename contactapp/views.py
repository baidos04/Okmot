from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics, viewsets

# from .forms import FeedbackForm
from .models import ContInfo, Feedback
from .serializers import ContInfoSerializer, FeedbackSerializer


class ContactappViewSet(viewsets.ModelViewSet):
    queryset = ContInfo.objects.all()
    serializer_class = ContInfoSerializer


class ContInfoListCreateView(generics.ListCreateAPIView):
    queryset = ContInfo.objects.all()
    serializer_class = ContInfoSerializer


class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
