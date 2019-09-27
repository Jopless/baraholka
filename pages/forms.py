from django import forms
from .models import Sneakers, Brand


class SneakersForm(forms.ModelForm):
    class Meta:
        model = Sneakers
        fields = ['model_name', 'model_price', 'model_brand']


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

