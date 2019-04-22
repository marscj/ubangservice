from django import forms

from phonenumber_field.formfields import PhoneNumberField

from .models import Company

class CompanyForm(forms.ModelForm):
    
    phone = PhoneNumberField(
        required=True,
        initial='+971',
        help_text='+971 XXX XXXXXXX'
    )

    tel = PhoneNumberField(
        required=True,
        initial='+971',
        help_text='+971 04-XXXXXXX'
    )

    class Meta:
        model = Company
        fields = '__all__'
    
