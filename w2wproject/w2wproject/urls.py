from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('news.urls')),
    path('api/', include('brands.urls')),
    path('api/', include('collaborations.urls')),
    path('api/', include('chat.urls')),
]
