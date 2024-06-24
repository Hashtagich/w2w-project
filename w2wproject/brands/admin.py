from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import brand, other, social_network


# Register your models here.

# INLINES

class BrandFotoInline(TabularInline):
    model = brand.FotoBrand
    fields = ('foto',)


class InterestInline(TabularInline):
    model = brand.BrandInterest
    fields = ('interest_id',)


class CategoryInline(TabularInline):
    model = brand.BrandCategory
    fields = ('category_id',)


class BrandSocialNetworkInline(TabularInline):
    model = social_network.SocialNetwork
    fields = ('name', 'link',)


# MODELS

@admin.register(brand.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'number_subscribers', 'average_check', 'avatar_id')

    inlines = (
        BrandFotoInline,
        CategoryInline,
        InterestInline,
        BrandSocialNetworkInline,
    )


@admin.register(brand.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_active')


@admin.register(other.AverageCheck)
class AverageCheckAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_active')


@admin.register(other.NumberSubscribers)
class NumberSubscribersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_active')


@admin.register(other.Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_active')


@admin.register(other.Predictions)
class PredictionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'prediction')


@admin.register(social_network.NameSocialNetwork)
class NameSocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_active')


@admin.register(social_network.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
