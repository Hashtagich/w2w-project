from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from brands.views.other import PredictionViewSet, PredictionAPIView
from brands.views.brand import ExperienceUpView

router = DefaultRouter()

urlpatterns = [
    path('prediction/', PredictionAPIView.as_view(), name='prediction'),
    path('predictions/', PredictionViewSet.as_view(), name='predictions'),
    path('experience_up/', ExperienceUpView.as_view(), name='experience_up'),
]
