# products/views.py
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm

# ---------------------------------
# 🏠 TAMPILAN HOME (Semua Produk)
# ---------------------------------
class HomeView(ListView):
    model = Product # Ambil data dari model Product
    template_name = 'home.html'
    context_object_name = 'products' # Nama variabel di HTML
    ordering = ['-created_at'] # Urutkan dari yang terbaru

# ---------------------------------
# 🔒 TAMPILAN DASHBOARD (Produk Milik Sendiri)
# ---------------------------------
class DashboardView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'dashboard.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        # Ini PENTING:
        # Filter produk agar hanya menampilkan
        # produk milik user yang sedang login.
        return Product.objects.filter(affiliator=self.request.user).order_by('-created_at')

# ---------------------------------
# ➕ TAMPILAN TAMBAH PRODUK (Form)
# ---------------------------------
class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm # Gunakan form yang kita buat tadi
    template_name = 'add_product.html'
    
    # Arahkan ke dashboard jika sukses menambah
    success_url = reverse_lazy('dashboard') 

    def form_valid(self, form):
        # Ini PENTING:
        # Isi field 'affiliator' secara otomatis
        # dengan user yang sedang login saat ini.
        form.instance.affiliator = self.request.user
        return super().form_valid(form)
    

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

# products/views.py

# 1. Tambahkan UpdateView, DeleteView, dan UserPassesTestMixin
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# ... (sisa impor lainnya)


# ... (Biarkan HomeView, DashboardView, AddProductView, ProductDetailView) ...


# ---------------------------------
# ✏️ TAMBAHKAN CLASS UNTUK UPDATE
# ---------------------------------
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_edit.html' # Kita akan buat file ini
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        # Fungsi keamanan: Cek apakah produk ini milik user yang sedang login
        product = self.get_object()
        return product.affiliator == self.request.user

# ---------------------------------
# 🗑️ TAMBAHKAN CLASS UNTUK DELETE
# ---------------------------------
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'product_delete_confirm.html' # Kita akan buat file ini
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        # Fungsi keamanan: Cek apakah produk ini milik user yang sedang login
        product = self.get_object()
        return product.affiliator == self.request.user