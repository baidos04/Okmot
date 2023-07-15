from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
print(router)

urlpatterns = [
    path('newsinf/', NewsListCreateView.as_view(), name='newsinflist'),
]
