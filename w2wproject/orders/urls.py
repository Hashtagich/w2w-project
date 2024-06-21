from django.urls import path
from .views import YookassaPayment

urlpatterns = [
    path('payment/<int:pk>/', YookassaPayment.as_view(), name='yookassa-payment'),
]