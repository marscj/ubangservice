from django import forms
from django.contrib.admin import widgets
from django.core.exceptions import ValidationError

from .models import Brand, Model, Vehicle
from .import CarCategory, BusCategory, VehicleType
from ubang.company import CompanyType

class ModelForm(forms.ModelForm):

    class Meta:
        model = Model
        fields = '__all__'

    def has_key(self, src, key):
        for s in src:
            if s[0] == key:
                return True

        return False

    def clean_category(self):
        category = self.cleaned_data['category']
        type = self.cleaned_data['type']

        if type == VehicleType.Car:
            if not self.has_key(CarCategory.CHOICES, category):
                raise ValidationError('Ensure category is a car category')
        else:
            if not self.has_key(BusCategory.CHOICES, category):
                raise ValidationError('Ensure category is a bus category')

        return category
    
class VehicleForm(forms.ModelForm):
    
    class Meta:
        model = Vehicle
        fields = '__all__'

    def clean_driver(self):
        driver = self.cleaned_data.get('driver')
        model = self.cleaned_data.get('model')

        if model and model.type == VehicleType.Bus and driver is None:
            raise ValidationError('This field is required.') 

        if driver and not driver.is_driver:
            raise ValidationError('Ensure user is a driver')

        if driver and driver.company is None:
            raise ValidationError('Ensure user is a company user')

        return driver

    def clean_company(self):
        data = self.cleaned_data.get('company')

        if data and data.type != CompanyType.Supplier:
            raise ValidationError('Ensure company type is supplier')
        
        return data
    
    

