# products/models.py
from django.db import models
from django.conf import settings 

class Product(models.Model):
    affiliator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE 
    )
    
    # Field-field yang kamu minta:
    name = models.CharField(max_length=255)
    price = models.BigIntegerField(default=0) # Ini HARGA produk
    store_name = models.CharField(max_length=100, blank=True, null=True) # Nama toko
    
    # Field ini diubah untuk menampung BANYAK URL
    image_urls = models.TextField(
        blank=True, 
        null=True,
        help_text="Masukkan satu URL gambar per baris."
    )
    
    description = models.TextField(blank=True, null=True)
    product_link = models.URLField(max_length=1024)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    # --- Fungsi Bantuan ---
    # Ini untuk memecah URL gambar di TextField menjadi daftar (list)
    def get_image_list(self):
        if self.image_urls:
            # Memecah string berdasarkan baris baru, dan memfilter baris kosong
            return [url.strip() for url in self.image_urls.splitlines() if url.strip()]
        return []

    # Ini untuk mengambil gambar pertama sebagai COVER
    def get_cover_image(self):
        images = self.get_image_list()
        if images:
            return images[0]
        # Sediakan gambar default jika tidak ada gambar
        return "https://via.placeholder.com/300.png?text=No+Image"