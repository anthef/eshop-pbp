from django.core.management.base import BaseCommand
from main.models import ProductEntry

class Command(BaseCommand):
    help = 'Add sample products to the database'

    def handle(self, *args, **kwargs):
        product1 = ProductEntry(name="Laptop", price=1200, description="A high-performance laptop.")
        product1.save()

        product2 = ProductEntry(name="Smartphone", price=800, description="A latest model smartphone.")
        product2.save()

        self.stdout.write(self.style.SUCCESS('Successfully added products'))
