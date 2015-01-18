from django.contrib import admin
from commerce.models import *


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'postcode', 'city', 'client')


class AddressInline(admin.StackedInline):
    model = Address
    extra = 1


class ClientAdmin(admin.ModelAdmin):
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
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
    readonly_fields = ('total',)
    fields = ()
    extra = 3

    def total(self, instance):
        if instance.id:
            return instance.total()
        else:
            return ""


class OrderAdmin(admin.ModelAdmin):
    def total(self, instance):
        total = 0
        order_details = OrderDetail.objects.filter(order__client_id=instance.client_id)
        for order_detail in order_details:
            total += order_detail.total()
        return total
    list_display = ('order_date', 'total', 'client', 'shipping_address')
    list_filter = ('client',)
    readonly_fields = ('total', 'stripe_charge_id')
    inlines = [
        OrderDetailInline,
    ]

admin.site.register(Client, ClientAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(VAT)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)