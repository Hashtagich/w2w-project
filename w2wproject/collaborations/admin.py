from django.contrib import admin
from django.contrib.admin import TabularInline
from brands.models import brand
from collaborations.models import Like, Match, Task, FotoCollaboration, Collaboration


# Register your models here.


# INLINES

class CollaborationFotoInline(TabularInline):
    model = FotoCollaboration
    fields = ('foto',)


class BrandInline(TabularInline):
    model = brand.BrandCollaboration
    fields = ('brand_id',)


class TaskInline(TabularInline):
    model = Task
    # readonly_fields = ('datetime_create',)
    fields = (
        'name', 'status', 'description', 'author',
        'datetime_start', 'datetime_completion',
        'datetime_finish',
    )


# MODELS

@admin.register(Collaboration)
class CollaborationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'number_subscribers', 'average_check', 'avatar_id', 'result')

    inlines = (
        BrandInline,
        CollaborationFotoInline,
        TaskInline,
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = (
        'name', 'status', 'description', 'author',
        'datetime_start', 'datetime_completion',
        'datetime_finish',
    )


admin.site.register(Like)
admin.site.register(Match)
