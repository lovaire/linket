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
            'category',        # ← Hanya nama field
            'image_urls', 
            'description', 
            'product_link', 
            'rating'
        ]
        
        # products/forms.py
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: Headset Gaming Keren'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: 150000'}),
            'store_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: Toko Jaya Abadi'}),
            'category': forms.Select(attrs={'class': 'form-control'}),  # INI PENTING!
            'image_urls': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Satu URL per baris...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Deskripsi singkat...'}),
            'product_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://s.shopee.co.id/...'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5, 'step': 0.1, 'placeholder': '4.8'}),
        }