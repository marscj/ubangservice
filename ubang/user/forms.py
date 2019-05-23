from django import forms
from django.contrib.auth import forms

from phonenumber_field.formfields import PhoneNumberField

from .models import CustomUser

class CustomUserCreationForm(forms.UserCreationForm):
    
    phone = PhoneNumberField(
        required=False,
        help_text='+971 XXX XXXXXXX'
    )

    class Meta:
        model = CustomUser
        fields = '__all__'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.save()
        return user
