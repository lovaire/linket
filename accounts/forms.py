# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    # Kita tambahkan field display_name ke form registrasi
    display_name = forms.CharField(max_length=150, required=False, help_text='Nama yang akan tampil ke publik.')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # Tambahkan 'display_name' ke fields yang akan ditampilkan
        fields = ('username', 'display_name', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'display_name', 'email')