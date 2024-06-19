from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from brands.views.other import PredictionAPIView
from brands.views.brand import (BrandAPIRetrieve, BrandAPIList)
from brands.views.social_network import *
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# brand
urlpatterns += [
    path('brands/', BrandAPIList.as_view(), name='prediction'),
    path('brand/<int:pk>/', BrandAPIRetrieve.as_view(), name='prediction'),
]

# other
urlpatterns += [
    path('prediction/', PredictionAPIView.as_view(), name='prediction'),
    # path('experience_up/', ExperienceUpView.as_view(), name='experience_up'),
]

# social_network
urlpatterns += [
    path('social_network/', SocialNetworkAPIList.as_view(), name='social_network'),
]
