# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic # Import 'generic'
from .forms import CustomUserCreationForm

class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    # Arahkan ke halaman login jika registrasi berhasil
    success_url = reverse_lazy('login') 
    template_name = 'registration/register.html'