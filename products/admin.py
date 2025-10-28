# products/admin.py
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    # Kolom apa saja yang tampil di daftar produk
    list_display = ('name', 'affiliator', 'category', 'marketplace', 'price', 'created_at')
    
    # Menambah filter di sisi kanan
    list_filter = ('category', 'marketplace', 'affiliator')
    
    # Menambah kotak pencarian
    search_fields = ('name', 'description', 'store_name')
    
    # Mengatur urutan field saat mengedit
    fieldsets = (
        (None, {
            'fields': ('name', 'affiliator', 'price')
        }),
        ('Kategorisasi', {
            'fields': ('category', 'marketplace', 'store_name')
        }),
        ('Detail Link', {
            'fields': ('product_link', 'image_urls', 'description', 'rating')
        }),
    )

admin.site.register(Product, ProductAdmin)