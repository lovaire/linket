# products/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 
            'price', 
            'store_name',
            'category',  # <-- TAMBAHKAN INI
            'image_urls', 
            'description', 
            'product_link', 
            'rating'
        ]
        
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Contoh: Headset Gaming Keren'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Contoh: 150000 (tanpa titik)'}),
            'store_name': forms.TextInput(attrs={'placeholder': 'Contoh: Toko Jaya Abadi'}),
            
            # Django otomatis render 'category' sebagai dropdown
            
            'image_urls': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Satu URL gambar per baris...'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Deskripsi singkat produk...'}),
            'product_link': forms.URLInput(attrs={'placeholder': 'https://s.shopee.co.id/link-afiliasi-kamu'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'step': 0.1, 'placeholder': 'Contoh: 4.8'}),
        }