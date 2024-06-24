from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from brands.views.brand import (BrandViewSet, BrandLevelUpView, BrandBalanceUpView, BrandExperienceUpView,
                                BrandModifierUpView, BrandsRecommendationsViewSet)
from brands.views.other import PredictionAPIView

router = DefaultRouter()

router.register(r'brand', BrandViewSet, basename='brand')

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# brand
urlpatterns += [
    path('brand/<int:pk>/modifier_up/', BrandModifierUpView.as_view(), name='brand-modifier-up'),
    path('brand/<int:pk>/level_up/', BrandLevelUpView.as_view(), name='brand-level-up'),
    path('brand/<int:pk>/balance_up/', BrandBalanceUpView.as_view(), name='brand-balance-up'),
    path('brand/<int:pk>/experience_up/', BrandExperienceUpView.as_view(), name='brand-experience-up'),
    path('brands_recommendations/', BrandsRecommendationsViewSet.as_view(), name='brands_recommendations'),
]

# other
urlpatterns += [
    path('prediction/', PredictionAPIView.as_view(), name='prediction'),
]
