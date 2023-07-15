from django.urls import path, include
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'home', HomeViewSet)

urlpatterns = [
    path('home/', HomeListCreateView.as_view(), name='home'),
]
