from django import forms
from django.core.exceptions import ValidationError

from collections import Counter

from phonenumber_field.formfields import PhoneNumberField

from .models import Order

# class UserInlineFormSet(BaseInlineFormSet):
    
#     def clean(self):
#         super().clean()

#         _list = []

#         for form in self.forms:
#             if form.cleaned_data and not form.cleaned_data.get('DELETE'):
#                 print(form.cleaned_data)
#                 if form.cleaned_data.get('user'):
#                     _list.append(form.cleaned_data['user'].username)
            
#         counter = Counter(_list).most_common()

#         if len(counter) > 0:
#             if counter[0][1] > 1:
#                 raise ValidationError('Please remove duplicate data')

class OrderForm(forms.ModelForm):
    
    contact_phone = PhoneNumberField(
        required=True,
        initial='+971',
        help_text='+971 XXX XXXXXXX'
    )

    class Meta:
        model = Order
        fields = '__all__'

    def clean_end_time(self):
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        
        if start_time and end_time:
            duration = end_time - start_time

            if start_time > end_time:
                raise ValidationError('Ensure start time is less than end time')
            
            if duration.total_seconds() < 3600:
                raise ValidationError('Ensure duration is greater than 1 hour')

        return end_time
    