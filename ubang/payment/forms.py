from django import forms

from .models import Payment

class PaymentCreatForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ('gateway', )
