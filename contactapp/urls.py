from django.urls import path
from rest_framework import routers
from django.contrib import admin

from .views import ContInfoListCreateView, ContInfoDetailView, FeedbackListCreateView, FeedbackDetailView, \
    ContactappViewSet
from . import views
# urlchik
router = routers.DefaultRouter()
router.register(r'contactapp', ContactappViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact-information/', ContInfoListCreateView.as_view(), name='contact-information-list'),
    path('contact-information/<int:pk>/', ContInfoDetailView.as_view(), name='contact-information-detail'),
    path('feedback/', FeedbackListCreateView.as_view(), name='feedback-list'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='feedback-detail'),
    path('success/', views.SuccessView.as_view(), name='success'),
]
