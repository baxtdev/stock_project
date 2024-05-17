from django.contrib import admin

# Register your models here.
from .models import Stock,Product,ProductPhoto,Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    list_per_page = 10


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ('product','created_at')
    search_fields = ('product',)
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    