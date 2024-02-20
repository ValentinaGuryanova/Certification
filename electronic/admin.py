from django.contrib import admin

from electronic.models import Contact, Product, Supplier, Seller


# admin.site.register(Contact)
# admin.site.register(Product)
# admin.site.register(Supplier)
# admin.site.register(Seller)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('city', 'country')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact')
