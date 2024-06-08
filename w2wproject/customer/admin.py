from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import customer, other, social_network, brand, collaboration  # , match,

admin.site.register(other.MagicBall)
#########
# INLINES
#########
class CustomerFotoInline(TabularInline):    
    model = customer.FotoCustomer
    fields = ('foto',)


class BrandFotoInline(TabularInline):
    model = brand.FotoBrand
    fields = ('foto',)


class CollaborationFotoInline(TabularInline):
    model = collaboration.FotoCollaboration
    fields = ('foto',)


class CustomerSocialNetworkInline(TabularInline):
    model = social_network.SocialNetwork
    fields = ('name', 'link',)


class InterestInline(TabularInline):
    model = customer.CustomerInterest
    fields = ('interest_id',)


class BrandInline(TabularInline):
    model = brand.BrandCollaboration
    fields = ('brand_id',)


class CategoryInline(TabularInline):
    model = brand.BrandCategory
    fields = ('category_id',)


class TaskInline(TabularInline):
    model = collaboration.Task
    # readonly_fields = ('datetime_create',)
    fields = (
        'name', 'status', 'description', 'author',
        'datetime_start', 'datetime_completion',
        'datetime_finish',
    )


########
# MODELS
########
@admin.register(customer.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'surname', 'patronymic', 'nickname', 'email', 'phone', 'balance', 'experience', 'level',
        'modifier', 'gender', 'status', 'tariff',)

    inlines = (
        CustomerFotoInline,
        CustomerSocialNetworkInline,
        InterestInline
    )


@admin.register(customer.Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'duration')


@admin.register(customer.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_active')


@admin.register(brand.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'number_subscribers', 'average_check', 'avatar_id')

    inlines = (
        BrandFotoInline,
        CategoryInline,
    )


@admin.register(brand.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_active')


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
    list_display = (
        'id', 'name', 'status', 'description',
        'datetime_start', 'datetime_completion', 'datetime_finish'
    )


@admin.register(other.AverageCheck)
class AverageCheckAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_active')


@admin.register(other.NumberSubscribers)
class NumberSubscribersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_active')


@admin.register(other.Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_active')


@admin.register(other.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')


@admin.register(social_network.NameSocialNetwork)
class NameSocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_active')


@admin.register(social_network.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')

# Для копирования
#     list_display = ('id', 'name', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
