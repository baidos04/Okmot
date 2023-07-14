from django.shortcuts import render

from rest_framework import viewsets
from .models import *
from .serializers import HistorySerializer, AdminContactSerializer, DeputiesSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class AdminContactViewSet(viewsets.ModelViewSet):
    queryset = AdminContact.objects.all()
    serializer_class = AdminContactSerializer

class DeputiesViewSet(viewsets.ModelViewSet):
    queryset = Deputies.objects.all()
    serializer_class = DeputiesSerializer

