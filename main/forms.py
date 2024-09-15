from django.forms import ModelForm
from .models import ProductEntry

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields=['name','price','description']