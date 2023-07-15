# from djangorestframework import generics
from rest_framework import generics

from .models import *
from .serializers import ContInfoSerializer, FeedbackSerializer


class ContInfoListCreateView(generics.ListCreateAPIView):
    queryset = ContInfo.objects.all()
    serializer_class = ContInfoSerializer


class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
