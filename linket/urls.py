# linket_core/urls.py
from django.contrib import admin
from django.urls import path, include # Pastikan 'include' ada di sini

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Meng-include URL bawaan Django (untuk login, logout)
    # Ini akan membuat URL seperti /accounts/login/
    path('accounts/', include('django.contrib.auth.urls')),
    
    # 2. Meng-include URL 'accounts' kustom kita (register)
    # Ini akan membuat URL /accounts/register/
    path('accounts/', include('accounts.urls')),
    
    # 3. Meng-include URL 'products' kita
    # Ini akan membuat URL /, /dashboard/, dan /add/
    path('', include('products.urls')), 
]