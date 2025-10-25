# products/urls.py
from django.urls import path
from .views import HomeView, DashboardView, AddProductView, ProductDetailView

urlpatterns = [
    # Ini membuat URL halaman utama: /
    path('', HomeView.as_view(), name='home'),
    
    # Ini membuat URL: /dashboard/
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    # Ini membuat URL: /add/
    path('add/', AddProductView.as_view(), name='add_product'),

    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]