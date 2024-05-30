from django.contrib import admin
from django.contrib.admin import TabularInline

from customer.models import customer, brand, collaboration, match, other, social_network


# Register your models here.

@admin.register(customer.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'surname', 'patronymic', 'nickname', 'email', 'phone', 'balance', 'experience', 'level',
        'modifier', 'gender', 'status', 'tariff')


@admin.register(customer.Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'duration')


@admin.register(customer.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort', 'is_active')

# @admin.register(customer.Customer)
# class ExhibitionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
