from django.urls import path
from .consumers import *


websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
    # path('ws/chat/<str:room_name>/notification/', NotificationConsumer.as_asgi()),
]