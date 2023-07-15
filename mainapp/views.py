from django.shortcuts import render

from rest_framework import viewsets, generics
from .models import Home
from .serializers import HomeSerializer

class HomeListCreateView(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

