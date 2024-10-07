# main/forms.py
from django.forms import ModelForm
from .models import ProductEntry
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ['name', 'price', 'description']

    def clean_name(self):
        name = self.cleaned_data["name"]
        name = strip_tags(name)
        if not name:
            raise ValidationError("Product name cannot be empty.")
        return name

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError("Price cannot be negative.")
        return price
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        description = strip_tags(description)
        return description
