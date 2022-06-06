from django.contrib import admin
from . models import seller,buyer,producat
# Register your models here.
# admin.site.register(seller)
# admin.site.register(buyer)
# admin.site.register(producat)


@admin.register(seller)
class sellerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone', 'date']


@admin.register(buyer)
class buyerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone', 'email', 'purchase_date']


@admin.register(producat)
class producatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dis', 'price', 'img']