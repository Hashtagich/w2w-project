from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import other

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]

# Other (FAQ)
urlpatterns += [
    path('faq/', other.FAQAPIList.as_view(), name='faq'),
]
