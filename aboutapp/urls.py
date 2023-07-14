from django.urls import path, include
from rest_framework import routers
from .views import HistoryViewSet, AdminContactViewSet, DeputiesViewSet

router = routers.DefaultRouter()
router.register(r'history', HistoryViewSet)
router.register(r'admincontact', AdminContactViewSet)
router.register(r'deputies', DeputiesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
