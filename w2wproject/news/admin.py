from django.contrib import admin
from .models import Post


# Register your models here.

# MODELS

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'avatar_id', 'link', 'is_active', 'datetime_create')

