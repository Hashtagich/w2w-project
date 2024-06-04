from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customer.views import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),
    path('api/auth/', include('dj_rest_auth.urls')),  # Обновлено
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Обновлено
]