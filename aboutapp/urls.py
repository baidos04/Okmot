from django.urls import path, include
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'history', HistoryViewSet)
# router.register(r'admincontact', AdminContactViewSet)
# router.register(r'deputies', DeputiesViewSet)

urlpatterns = [
    path('historylist/', HistoryListCreateView.as_view(), name='historylist'),
    path('adminlist/', AdminListCreateView.as_view(), name='adminlist'),
    path('deplist/', DeputiesListCreateView.as_view(), name='deplist'),
]

