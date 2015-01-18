from django.contrib import admin
from commerce.models import *

class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'postcode', 'city', 'client')

class AddressInline(admin.StackedInline):
    model = Address
    extra = 1

class ClientAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline,
    ]

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline
    ]

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 3

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderDetailInline,
    ]

admin.site.register(Client, ClientAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(VAT)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order,OrderAdmin)