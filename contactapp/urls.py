from django.urls import path
from rest_framework import routers
from django.contrib import admin

from .views import *
from . import views


router = routers.DefaultRouter()
router.register(r'contactapp', ContactappViewSet)

urlpatterns = [
    path('contact-information/', ContInfoListCreateView.as_view(), name='contact-information-list'),
    path('feedback/', FeedbackListCreateView.as_view(), name='feedback-list'),
]
