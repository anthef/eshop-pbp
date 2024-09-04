from django.contrib import admin
from .models import ProductEntry

@admin.register(ProductEntry)
class ProductEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
