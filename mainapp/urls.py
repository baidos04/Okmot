from django.urls import path, include
from rest_framework import routers
from .views import HomeViewSet

router = routers.DefaultRouter()
router.register(r'home', HomeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
