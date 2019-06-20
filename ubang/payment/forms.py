from django import forms

from djmoney.forms import MoneyField
from .models import Payment

class PaymentCreatForm(forms.ModelForm):

    total = MoneyField()
    captured_amount = MoneyField()
    
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentInlineFormset(forms.models.BaseFormSet):

    class Meta:
        model = Payment
        fields = ('gateway', )
