from django.urls import path
from .views import *

urlpatterns = [
    path('contact-information/', ContInfoListCreateView.as_view(), name='contact-information-list'),
    path('feedback/', FeedbackListCreateView.as_view(), name='feedback-list'),
]
