# products/views.py
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

# Import models dan form DI ATAS
from .models import CATEGORY_CHOICES, Product, MARKETPLACE_CHOICES
from .forms import ProductForm


# ---------------------------------
# 🏠 TAMPILAN HOME (Semua Produk)
# ---------------------------------
class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    ordering = ['-created_at']
    paginate_by = 18

    def get_queryset(self):
        search_query = self.request.GET.get('q', None)
        category_query = self.request.GET.get('category', None)
        marketplace_query = self.request.GET.get('marketplace', None)
        
        queryset = super().get_queryset()

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        if category_query and category_query != 'all':
            queryset = queryset.filter(category=category_query)

        if marketplace_query and marketplace_query != 'all': # <-- Tambah blok ini
            queryset = queryset.filter(marketplace=marketplace_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES  # Sekarang aman!
        context['marketplaces'] = MARKETPLACE_CHOICES
        context['search_query'] = self.request.GET.get('q', '')
        context['selected_category'] = self.request.GET.get('category', 'all')
        context['selected_marketplace'] = self.request.GET.get('marketplace', 'all')
        return context


# ---------------------------------
# 🔒 DASHBOARD (Produk Milik Sendiri)
# ---------------------------------
class DashboardView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'dashboard.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.filter(affiliator=self.request.user).order_by('-created_at')


# ---------------------------------
# ➕ TAMBAH PRODUK
# ---------------------------------
class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('dashboard') 

    def form_valid(self, form):
        form.instance.affiliator = self.request.user
        return super().form_valid(form)


# ---------------------------------
# 📄 DETAIL PRODUK
# ---------------------------------
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


# ---------------------------------
# ✏️ EDIT PRODUK
# ---------------------------------
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_edit.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        product = self.get_object()
        return product.affiliator == self.request.user


# ---------------------------------
# 🗑️ HAPUS PRODUK
# ---------------------------------
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'product_delete_confirm.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        product = self.get_object()
        return product.affiliator == self.request.user