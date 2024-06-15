from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import collaboration


# Register your models here.


# INLINES

class CollaborationFotoInline(TabularInline):
    model = collaboration.FotoCollaboration
    fields = ('foto',)


class TaskInline(TabularInline):
    model = collaboration.Task
    # readonly_fields = ('datetime_create',)
    fields = (
        'name', 'status', 'description',
        'datetime_start', 'datetime_completion',
        'datetime_finish',
    )


# MODELS

@admin.register(collaboration.Collaboration)
class CollaborationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'number_subscribers', 'average_check', 'avatar_id', 'result')

    inlines = (
        CollaborationFotoInline,
        TaskInline,
    )
