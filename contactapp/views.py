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


# class ContInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ContInfo.objects.all()
#     serializer_class = ContInfoSerializer


class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


# class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedbackSerializer

#
# class FeedbackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback.html', {'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#         return render(request, 'feedback.html', {'form': form})
#
#
# class SuccessView(View):
#     def get(self, request):
#         return render(request, 'success.html')

