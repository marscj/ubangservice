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

    def clean_brand(self):
        data = self.cleaned_data.get('brand')

        if data is None:
            raise ValidationError('This field is required')
         
        return data
    
class VehicleForm(forms.ModelForm):
    
    class Meta:
        model = Vehicle
        fields = '__all__'

    def clean_driver(self):
        driver = self.cleaned_data.get('driver')
        # if model and model.type == VehicleType.Bus and driver is None and is_actived:
        #     raise ValidationError('This field is required') 

        if driver and not driver.is_driver:
            raise ValidationError('Ensure user is a driver')

        if driver and driver.company is None:
            raise ValidationError('Ensure user is a company user')

        return driver
    
    def clean_is_actived(self):
        is_actived = self.cleaned_data.get('is_actived')
        driver = self.cleaned_data.get('driver')
        model = self.cleaned_data.get('model')

        if model is not None and model.type == VehicleType.Bus and driver is None and is_actived:
            raise ValidationError('Asif , if you want actived this vehicle, driver is must be not none') 
        
        return is_actived

    def clean_model(self):
        model = self.cleaned_data.get('model')

        if model is None:
            raise ValidationError('This field is required')

        return model

    def clean_company(self):
        data = self.cleaned_data.get('company')

        if data is None:
            raise ValidationError('This field is required')
        elif data.type != CompanyType.Supplier:
            raise ValidationError('Ensure company type is supplier')
        
        return data

    # def clean(self):
    #     data = self.cleaned_data
    #     driver = data.get('driver')
    #     model = data.get('model')
    #     is_actived = data.get('is_actived')

    #     if model is not None and model.type == VehicleType.Bus and driver is None and is_actived:
    #         raise ValidationError('Driver is required') 

    #     if driver is not None and not driver.is_driver:
    #         raise ValidationError('Ensure user is a driver')

    #     if driver is not None and driver.company is None:
    #         raise ValidationError('Ensure user is a company user')

    #     return data
    

