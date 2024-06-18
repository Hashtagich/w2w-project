from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import collaboration
from brands.models import brand
from .models.match import Like, Match, Chat, Message


# Register your models here.


# INLINES

class CollaborationFotoInline(TabularInline):
    model = collaboration.FotoCollaboration
    fields = ('foto',)


class BrandInline(TabularInline):
    model = brand.BrandCollaboration
    fields = ('brand_id',)


class TaskInline(TabularInline):
    model = collaboration.Task
    # readonly_fields = ('datetime_create',)
    fields = (
        'name', 'status', 'description', 'author',
        'datetime_start', 'datetime_completion',
        'datetime_finish',
    )


# MODELS

@admin.register(collaboration.Collaboration)
class CollaborationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'number_subscribers', 'average_check', 'avatar_id', 'result')

    inlines = (
        BrandInline,
        CollaborationFotoInline,
        TaskInline,
    )


@admin.register(collaboration.Task)
class TaskAdmin(admin.ModelAdmin):
    fields = (
        'name', 'status', 'description', 'author',
        'datetime_start', 'datetime_completion',
        'datetime_finish',
    )



admin.site.register(Like)
admin.site.register(Match)
admin.site.register(Chat)
admin.site.register(Message)
