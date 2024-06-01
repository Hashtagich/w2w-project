from django.contrib import admin
from django.contrib.admin import TabularInline

from customer.models import customer, brand, collaboration, match, other, social_network


# INLINES
class CustomerFotoInline(TabularInline):
    model = customer.FotoCustomer
    fields = ('foto',)

# class SocialNetworkInline(TabularInline):
#     model = social_network.SocialNetwork
#     fields = ('name', 'link')


# MODELS

@admin.register(customer.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'surname', 'patronymic', 'nickname', 'email', 'phone', 'balance', 'experience', 'level',
        'modifier', 'gender', 'status', 'tariff')

    inlines = (CustomerFotoInline,)


@admin.register(customer.Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'duration')


@admin.register(customer.Role)
class RoleAdmin(admin.ModelAdmin):
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


@admin.register(other.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')


@admin.register(social_network.NameSocialNetwork)
class NameSocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_active')


@admin.register(social_network.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
# @admin.register(customer.Customer)
# class ExhibitionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
