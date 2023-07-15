from django.shortcuts import render

from rest_framework import viewsets, generics
from .models import *
from .serializers import HistorySerializer, AdminContactSerializer, DeputiesSerializer



class HistoryListCreateView(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class AdminListCreateView(generics.ListCreateAPIView):
    queryset = AdminContact.objects.all()
    serializer_class = AdminContactSerializer


class DeputiesListCreateView(generics.ListCreateAPIView):
    queryset = Deputies.objects.all()
    serializer_class = DeputiesSerializer

